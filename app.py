import streamlit as st
import pandas as pd
import joblib
import sqlite3
import hashlib
import os
from datetime import datetime
from pathlib import Path
from disease_info import get_disease_info

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

# ---------------- FILE PATHS ----------------

BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = BASE_DIR / "dataset" / "Training.csv"
MODEL_PATH = BASE_DIR / "model" / "disease_model.pkl"
DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "users.db"

DATABASE_DIR.mkdir(exist_ok=True)

# ---------------- DATABASE ----------------

def get_db():
    conn = sqlite3.connect(str(DATABASE_PATH))
    conn.row_factory = sqlite3.Row
    return conn


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


# ---------------- PASSWORD SECURITY ----------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---------------- LOAD MODEL AND DATASET ----------------

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_dataset():
    df = pd.read_csv(DATASET_PATH)
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    if "prognosis" not in df.columns:
        raise ValueError("The dataset must contain a 'prognosis' column.")

    return df


try:
    model = load_model()
    data = load_dataset()

    symptoms = list(data.drop("prognosis", axis=1).columns)

    # Keep the same feature order used when training the model.
    if hasattr(model, "feature_names_in_"):
        symptoms = list(model.feature_names_in_)

except Exception as e:
    st.error("Unable to load the model or dataset.")
    st.write("Please check that these files are uploaded to GitHub:")
    st.code("dataset/Training.csv\nmodel/disease_model.pkl")
    st.write("Error details:", str(e))
    st.stop()


# ---------------- SESSION STATE ----------------

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "username" not in st.session_state:
    st.session_state.username = None


# ---------------- REGISTRATION ----------------

def register_user():
    st.title("📝 Create Your Account")
    st.write("Register to use the Disease Prediction System.")

    with st.form("register_form"):
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        submitted = st.form_submit_button("Register")

    if submitted:
        username = username.strip()
        email = email.strip()

        if not username or not email or not password:
            st.error("Please fill in all fields.")

        elif password != confirm_password:
            st.error("Passwords do not match.")

        elif len(password) < 6:
            st.error("Password must contain at least 6 characters.")

        else:
            conn = get_db()

            try:
                conn.execute(
                    """
                    INSERT INTO users (username, email, password)
                    VALUES (?, ?, ?)
                    """,
                    (username, email, hash_password(password))
                )

                conn.commit()
                st.success("Registration successful! Please log in.")

            except sqlite3.IntegrityError:
                st.error("Username or email already exists.")

            finally:
                conn.close()


# ---------------- LOGIN ----------------

def login_user():
    st.title("🔐 User Login")
    st.write("Login to access the Disease Prediction System.")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Login")

    if submitted:
        conn = get_db()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username.strip(),)
        ).fetchone()

        conn.close()

        if user and user["password"] == hash_password(password):
            st.session_state.user_id = user["id"]
            st.session_state.username = user["username"]

            st.success("Login successful!")
            st.rerun()

        else:
            st.error("Invalid username or password.")


# ---------------- HOME / DISEASE PREDICTION ----------------

def prediction_page():
    st.title("🩺 Disease Prediction System")

    st.write(
        "Select your symptoms below to get a machine-learning-based "
        "disease prediction."
    )

    st.info(
        "Select all symptoms that apply. You can search for symptoms "
        "inside the selection box."
    )

    selected_symptoms = st.multiselect(
        "Search and select your symptoms",
        options=symptoms,
        help="Type a symptom name to search for it."
    )

    if st.button("Predict Disease", type="primary"):

        if not selected_symptoms:
            st.warning("Please select at least one symptom.")

        else:
            # Convert selected symptoms into model input.
            input_data = pd.DataFrame(
                [[
                    1 if symptom in selected_symptoms else 0
                    for symptom in symptoms
                ]],
                columns=symptoms
            )

            try:
                prediction = model.predict(input_data)[0]
                disease = str(prediction).strip()

                st.success("Prediction completed!")

                st.subheader("Predicted Disease")
                st.markdown(f"## 🩺 {disease}")

                # Display prediction probabilities.
                if hasattr(model, "predict_proba"):
                    probabilities = model.predict_proba(input_data)[0]
                    classes = model.classes_

                    results = sorted(
                        zip(classes, probabilities),
                        key=lambda x: x[1],
                        reverse=True
                    )[:3]

                    st.subheader("Top 3 Predictions")

                    for disease_name, probability in results:
                        st.write(
                            f"**{str(disease_name).strip()}** — "
                            f"{probability * 100:.2f}%"
                        )

                        st.progress(float(probability))

                # Display disease information.
                st.divider()
                st.subheader("📖 Disease Information")

                info = get_disease_info(disease)

                if info:
                    sections = {
                        "overview": "Overview",
                        "causes": "Causes",
                        "symptoms": "Symptoms",
                        "risk_factors": "Risk Factors",
                        "precautions": "Precautions",
                        "prevention": "Prevention",
                        "doctor": "When to Consult a Doctor"
                    }

                    for key, heading in sections.items():
                        if info.get(key):
                            with st.expander(heading, expanded=(key == "overview")):
                                st.write(info[key])

                else:
                    st.warning(
                        "Detailed information is not available "
                        "for this disease yet."
                    )

                # Save prediction history.
                conn = get_db()

                conn.execute(
                    """
                    INSERT INTO history
                    (user_id, symptoms, disease, date)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        st.session_state.user_id,
                        ", ".join(selected_symptoms),
                        disease,
                        datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    )
                )

                conn.commit()
                conn.close()

                st.success("Prediction saved in your history.")

                st.warning(
                    "Disclaimer: This project is for educational purposes "
                    "only. Predictions are not medical diagnoses. "
                    "Consult a qualified healthcare professional."
                )

            except Exception as e:
                st.error("Prediction failed.")
                st.write(str(e))


# ---------------- PREDICTION HISTORY ----------------

def history_page():
    st.title("📋 My Prediction History")

    conn = get_db()

    records = conn.execute(
        """
        SELECT symptoms, disease, date
        FROM history
        WHERE user_id = ?
        ORDER BY id DESC
        """,
        (st.session_state.user_id,)
    ).fetchall()

    conn.close()

    if records:
        history_df = pd.DataFrame(
            [dict(record) for record in records]
        )

        history_df.columns = [
            "Symptoms",
            "Predicted Disease",
            "Date"
        ]

        st.dataframe(
            history_df,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("You have not made any predictions yet.")


# ---------------- MAIN APPLICATION ----------------

def main():

    if st.session_state.user_id is None:

        st.title("🩺 Disease Prediction Using Machine Learning")

        st.write(
            "Welcome! Register or log in to predict diseases "
            "based on selected symptoms."
        )

        choice = st.radio(
            "Choose an option",
            ["Login", "Register"],
            horizontal=True
        )

        if choice == "Login":
            login_user()
        else:
            register_user()

    else:

        st.sidebar.title("Disease Prediction System")

        st.sidebar.write(
            f"Welcome, **{st.session_state.username}**!"
        )

        page = st.sidebar.radio(
            "Navigation",
            ["Disease Prediction", "Prediction History"]
        )

        if st.sidebar.button("Logout"):
            st.session_state.user_id = None
            st.session_state.username = None
            st.rerun()

        if page == "Disease Prediction":
            prediction_page()

        elif page == "Prediction History":
            history_page()


if __name__ == "__main__":
    main()