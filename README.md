# 💳 Fraud Detection System

A Machine Learning-based Fraud Detection System built using XGBoost, Streamlit, and FastAPI. This project predicts fraudulent credit card transactions in real-time and provides an interactive dashboard for analytics and visualization.

---

# 🚀 Features

- ✅ Real-time Fraud Detection
- ✅ Interactive Streamlit Dashboard
- ✅ Fraud Probability Prediction
- ✅ Dataset Analytics & Visualization
- ✅ FastAPI Backend Integration
- ✅ SQLite Database Logging
- ✅ Deployment Ready

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Programming Language |
| Streamlit | Frontend Dashboard |
| XGBoost | Machine Learning Model |
| Scikit-learn | Data Preprocessing & Evaluation |
| FastAPI | Backend API |
| Plotly | Interactive Charts |
| Pandas | Data Handling |
| SQLite | Database Logging |

---

# 📂 Project Structure

```bash
fraud-detection-system/
│
├── app/
│   ├── main.py
│   ├── predict.py
│   ├── preprocessing.py
│   └── utils.py
│
├── dashboard/
│   └── streamlit_app.py
│
├── api/
│   └── api.py
│
├── models/
│   ├── fraud_model.pkl
│   └── scaler.pkl
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

This project uses the **Credit Card Fraud Detection Dataset**.

### Dataset Source
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Note
The dataset file is not uploaded to GitHub due to file size limitations.

After downloading the dataset, place:

```bash
creditcard.csv
```

inside the `data/` folder.

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## 2️⃣ Move Into Project Folder

```bash
cd fraud-detection-system
```

---

## 3️⃣ Create Virtual Environment

```bash
py -3.14 -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Running the Project

# ▶️ Train the Model

```bash
cd app
python main.py
```

This generates:

```bash
models/fraud_model.pkl
models/scaler.pkl
```

---

# ▶️ Run Streamlit App

Go back to root folder:

```bash
cd ..
```

Run:

```bash
streamlit run dashboard/streamlit_app.py
```

Open in browser:

```bash
http://localhost:8501
```

---

# 🌐 Run FastAPI Backend

```bash
uvicorn api.api:app --reload
```

Open API Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# 📈 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Scaling
4. Handling Imbalanced Dataset using SMOTE
5. Model Training using XGBoost
6. Model Evaluation
7. Real-time Fraud Prediction

---

# 📊 Model Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

# 🌍 Live Demo

### Streamlit App
Add your deployed Streamlit link here:

```bash
https://your-streamlit-app-link.streamlit.app
```

---

# 👩‍💻 Author

### Madhu Ritha

Machine Learning & Data Analytics Enthusiast

---



