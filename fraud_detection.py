import streamlit as st
import pandas as pd
import joblib

model = joblib.load('fraud_detector_pipeline.pkl')

st.title("Credit Card Fraud Detection on a 6 million+ dataset")

st.markdown("Please enter the details of the transaction to predict if it's fraudulent or not.")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])

amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance Origin (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance Origin (Sender)", min_value=0.0, value=9000.0)

oldbalanceDest = st.number_input("Old Balance Destination (Receiver)", min_value=0.0, value=5000.0)
newbalanceDest = st.number_input("New Balance Destination (Receiver)", min_value=0.0, value=6000.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : {int(prediction)}")

    if prediction == 1:
        st.error("The transaction is predicted to be FRAUDULENT.")
    else:
        st.success("The transaction is predicted to be LEGITIMATE.")