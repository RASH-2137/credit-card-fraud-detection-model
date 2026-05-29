# Credit Card Fraud Detection System

A Machine Learning based Credit Card Fraud Detection System built using **Logistic Regression**, **Scikit-learn Pipeline**, and **Streamlit**.
The model is trained on a **6 million+ transaction dataset** from Kaggle to classify financial transactions as fraudulent or legitimate.

---
## Live Demo

Try the deployed application here:

[Credit Card Fraud Detection App]((https://creditcard-fraud-detection2.streamlit.app/))


## Features

* Fraud detection using Machine Learning
* Built with Logistic Regression
* End-to-end preprocessing pipeline
* Streamlit web application interface
* Real-time transaction prediction
* Handles numerical and categorical transaction data
* Trained on large-scale financial transaction dataset

---

## Tech Stack

* Python
* Scikit-learn
* Pandas
* NumPy
* Streamlit
* Joblib

---

## Machine Learning Pipeline

The project uses a Scikit-learn Pipeline with:

* ColumnTransformer
* StandardScaler
* Logistic Regression

The pipeline automates:

* Data preprocessing
* Feature scaling
* Model training
* Prediction workflow

---

## Dataset

* Source: Kaggle
* Dataset Size: 6M+ transactions
* Type: Financial transaction dataset for fraud detection

The dataset includes:

* Transaction type
* Transaction amount
* Sender balances
* Receiver balances
* Fraud labels

---

## Model Performance

| Metric   | Score |
| -------- | ----- |
| Accuracy | 94%   |

---

## Project Structure

```bash
Credit-Card-Fraud-Detection/
│
├── fraud_detection.py
├── fraud_detector_pipeline.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/credit-card-fraud-detection-model.git
```

### Navigate to Project Folder

```bash
cd credit-card-fraud-detection-model
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run fraud_detection.py
```

---

## Application Preview

The Streamlit application allows users to:

* Enter transaction details
* Predict whether a transaction is fraudulent
* Get instant classification results

---

## Future Improvements

* Add fraud probability score
* Deploy using Docker
* Add visual analytics dashboard
* Improve model recall for fraud cases
* Implement advanced models like XGBoost or Neural Networks
* Add database integration

---

## Learning Outcomes

Through this project, I learned:

* End-to-end ML workflow
* Data preprocessing pipelines
* Feature scaling
* Model deployment using Streamlit
* GitHub project management
* Real-world fraud detection concepts

---

## Author

Rahul Sharma

GitHub: https://github.com/RASH-2137
