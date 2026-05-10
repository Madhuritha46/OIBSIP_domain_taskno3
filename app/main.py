import joblib

from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from preprocessing import load_data
from preprocessing import preprocess_data

DATA_PATH = "../data/creditcard.csv"


def train_model():

    print("Loading Dataset...")

    df = load_data(DATA_PATH)

    print("Preprocessing Data...")

    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

    print("Training Model...")

    model = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric='logloss',
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Accuracy: {accuracy}")

    print("\\nClassification Report:\\n")

    print(classification_report(y_test, predictions))

    print("\\nConfusion Matrix:\\n")

    print(confusion_matrix(y_test, predictions))

    joblib.dump(model, "../models/fraud_model.pkl")

    joblib.dump(scaler, "../models/scaler.pkl")

    print("Model Saved Successfully!")


if __name__ == "__main__":

    train_model()