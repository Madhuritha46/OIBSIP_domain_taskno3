import streamlit as st
import pandas as pd
import plotly.express as px

import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)

from app.predict import predict_transaction
from app.utils import create_database
from app.utils import insert_log

# Create database
create_database()

# Page Config
st.set_page_config(
    page_title="Fraud Detection System",
    layout="wide"
)

# Title
st.title("💳 Credit Card Fraud Detection System")

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Dataset Insights",
        "Fraud Prediction"
    ]
)

# HOME PAGE
if page == "Home":

    st.header("🏠 Home")

    st.write("""
    Advanced Fraud Detection System using Machine Learning and XGBoost.
    
    Features:
    - Real-time fraud prediction
    - Interactive dashboard
    - Fraud analytics
    - Database logging
    - Machine learning model
    """)

# DATASET INSIGHTS PAGE
elif page == "Dataset Insights":

    st.header("📊 Dataset Insights")

    df = pd.read_csv("data/creditcard.csv")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Fraud Distribution")

    fig = px.histogram(
        df,
        x="Class",
        title="Fraud vs Legitimate Transactions"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Transaction Amount Distribution")

    fig2 = px.box(
        df,
        y="Amount",
        title="Transaction Amount Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

# FRAUD PREDICTION PAGE
elif page == "Fraud Prediction":

    st.header("🔍 Fraud Prediction")

    st.write("Enter transaction details below:")

    feature_inputs = []

    feature_names = [
        "Time",
        "V1", "V2", "V3", "V4", "V5", "V6", "V7",
        "V8", "V9", "V10", "V11", "V12", "V13",
        "V14", "V15", "V16", "V17", "V18", "V19",
        "V20", "V21", "V22", "V23", "V24", "V25",
        "V26", "V27", "V28",
        "Amount"
    ]

    for feature in feature_names:

        value = st.number_input(
            feature,
            value=0.0
        )

        feature_inputs.append(value)

    if st.button("Predict Fraud"):

        prediction, probability = predict_transaction(feature_inputs)

        probability_percent = round(probability * 100, 2)

        if prediction == 1:

            st.error(
                f"⚠ Fraudulent Transaction Detected ({probability_percent}% confidence)"
            )

            result = "Fraud"

        else:

            st.success(
                f"✅ Legitimate Transaction ({probability_percent}% confidence)"
            )

            result = "Legitimate"

        # Save prediction to database
        insert_log(result, probability_percent)

        st.subheader("Fraud Probability")

        st.progress(int(probability_percent))

        st.write(f"Fraud Probability: {probability_percent}%")