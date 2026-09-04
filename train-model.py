import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib


# Load the credit-risk dataset
data = pd.read_csv("data/credit_data.csv")


# Separate input variables from the target
X = data.drop("credit_risk", axis=1)
y = data["credit_risk"]


# Identify categorical and numerical columns
categorical_features = [
    "employment",
    "credit_history"
]

numerical_features = [
    "age",
    "monthly_income",
    "loan_amount",
    "existing_debt",
    "loan_term"
]


# Prepare the data
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# Create the machine-learning model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Create the complete machine-learning pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Train the model
pipeline.fit(X_train, y_train)


# Test the model
predictions = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, predictions))


# Save the trained model
joblib.dump(
    pipeline,
    "credit_risk_model.pkl"
)

print("\nModel saved as credit_risk_model.pkl")
