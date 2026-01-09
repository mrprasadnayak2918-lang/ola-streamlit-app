import streamlit as st
import pandas as pd

@st.cache_data
def load():
    return pd.read_csv("OLA_DataSet_CLEANED.csv")

df = load()

st.title("❌ Cancellations")

customer = df[df["Booking_Status"].str.contains("Customer", na=False)]
driver = df[df["Booking_Status"].str.contains("Driver", na=False)]

st.subheader("Customer Cancellation Reasons")
st.bar_chart(customer["Cancellation_Reason_Customer"].fillna("Unknown").value_counts())

st.subheader("Driver Cancellation Reasons")
st.bar_chart(driver["Cancellation_Reason_Driver"].fillna("Unknown").value_counts())

