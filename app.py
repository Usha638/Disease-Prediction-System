from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model/disease_model.pkl")

# Load dataset
data = pd.read_csv("dataset/Training.csv")

# Remove unnecessary columns
data = data.loc[:, ~data.columns.str.contains("^Unnamed")]

# Get symptom names
symptoms = list(data.drop("prognosis", axis=1).columns)


@app.route("/")
def home():
    return render_template("index.html", symptoms=symptoms)


@app.route("/predict", methods=["POST"])
def predict():

    selected_symptoms = request.form.getlist("symptoms")

    if not selected_symptoms:
        return render_template(
            "index.html",
            symptoms=symptoms,
            error="Please select at least one symptom."
        )

    input_data = pd.DataFrame(
        [[1 if symptom in selected_symptoms else 0
          for symptom in symptoms]],
        columns=symptoms
    )

    prediction = model.predict(input_data)

    disease = prediction[0]

    return render_template(
        "index.html",
        symptoms=symptoms,
        prediction=disease
    )


if __name__ == "__main__":
    app.run(debug=True)