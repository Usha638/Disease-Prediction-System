

from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import joblib
import sqlite3
import os

from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import datetime

# Import disease information
from disease_info import get_disease_info


app = Flask(__name__)
app.secret_key = "change-this-to-a-long-random-secret"

# Create database folder
os.makedirs("database", exist_ok=True)


# Database connection
def get_db():
    conn = sqlite3.connect("database/users.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create database tables
def create_tables():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            symptoms TEXT NOT NULL,
            disease TEXT NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


create_tables()


# Load machine learning model
model = joblib.load("model/disease_model.pkl")

# Load dataset
data = pd.read_csv("dataset/Training.csv")

# Remove unwanted columns
data = data.loc[:, ~data.columns.str.contains("^Unnamed")]

# Get symptom names
symptoms = list(data.drop("prognosis", axis=1).columns)


# Login required decorator
def login_required(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))

        return route(*args, **kwargs)

    return wrapper


# Home page
@app.route("/")
@login_required
def home():
    return render_template(
        "index.html",
        symptoms=symptoms,
        username=session["username"]
    )


# Registration
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        if not username or not email or not password:
            return "Please fill all fields."

        hashed_password = generate_password_hash(password)

        conn = get_db()

        try:
            conn.execute(
                """
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
                """,
                (username, email, hashed_password)
            )

            conn.commit()

        except sqlite3.IntegrityError:
            conn.close()
            return "Username or email already exists."

        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()
        password = request.form["password"]

        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        conn.close()

        if user and check_password_hash(user["password"], password):

            session.clear()
            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("home"))

        return render_template(
            "login.html",
            error="Invalid username or password."
        )

    return render_template("login.html")


# Logout
@app.route("/logout")
@login_required
def logout():

    session.clear()

    return redirect(url_for("login"))


# Disease prediction
@app.route("/predict", methods=["POST"])
@login_required
def predict():

    selected_symptoms = request.form.getlist("symptoms")

    if not selected_symptoms:

        return render_template(
            "index.html",
            symptoms=symptoms,
            username=session["username"],
            error="Please select at least one symptom."
        )

    # Prepare input for machine learning model
    input_data = pd.DataFrame(
        [[1 if symptom in selected_symptoms else 0
          for symptom in symptoms]],
        columns=symptoms
    )

    # Predict disease
    prediction = model.predict(input_data)

    disease = prediction[0]

    # Get detailed disease information
    disease_details = get_disease_info(disease)

    # Save prediction in database
    conn = get_db()

    conn.execute(
        """
        INSERT INTO history (user_id, symptoms, disease, date)
        VALUES (?, ?, ?, ?)
        """,
        (
            session["user_id"],
            ", ".join(selected_symptoms),
            disease,
            datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        )
    )

    conn.commit()
    conn.close()

    # Display prediction and disease information
    return render_template(
        "index.html",
        symptoms=symptoms,
        username=session["username"],
        prediction=disease,
        disease_info=disease_details
    )


# Prediction history
@app.route("/history")
@login_required
def history():

    conn = get_db()

    records = conn.execute(
        """
        SELECT symptoms, disease, date
        FROM history
        WHERE user_id = ?
        ORDER BY id DESC
        """,
        (session["user_id"],)
    ).fetchall()

    conn.close()

    return render_template(
        "history.html",
        records=records
    )


# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)
