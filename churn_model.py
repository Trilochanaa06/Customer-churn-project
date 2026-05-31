import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv("customers.csv")
print(df["is_churned"].value_counts())
print(df["is_churned"].value_counts(normalize=True))

encoder = LabelEncoder()
df["subscription_type"] = encoder.fit_transform(df["subscription_type"])

X = df[
    [
        "monthly_spend",
        "login_frequency",
        "support_tickets",
        "days_inactive",
        "subscription_type"
    ]
]

y = df["is_churned"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    min_samples_split=5,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy:.2f}")
from sklearn.metrics import classification_report

print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, predictions))