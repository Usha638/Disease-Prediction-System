import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("dataset/Training.csv")

# Remove unnecessary columns
data = data.loc[:, ~data.columns.str.contains("^Unnamed")]

# Separate input and output
X = data.drop("prognosis", axis=1)
y = data["prognosis"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Training Completed!")
print("Accuracy:", accuracy * 100, "%")

# Classification report
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model/disease_model.pkl")

print("Model saved successfully!")