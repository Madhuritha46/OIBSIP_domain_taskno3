import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from imblearn.over_sampling import SMOTE


def load_data(path):

    df = pd.read_csv(path)

    return df


def preprocess_data(df):

    X = df.drop("Class", axis=1)

    y = df["Class"]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    smote = SMOTE(random_state=42)

    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled,
        y_resampled,
        test_size=0.2,
        random_state=42,
        stratify=y_resampled
    )

    return X_train, X_test, y_train, y_test, scaler