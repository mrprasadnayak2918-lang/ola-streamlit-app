import streamlit as st
import pandas as pd

@st.cache_data
def load():
    return pd.read_csv("OLA_DataSet_CLEANED.csv")

df = load()

st.title("💰 Revenue Analysis")

success = df[df["Booking_Status"].str.contains("Success", na=False)]

payment = success.groupby("Payment_Method")["Booking_Value"].sum()
st.bar_chart(payment)

vehicle_rev = success.groupby("Vehicle_Type")["Booking_Value"].sum()
st.bar_chart(vehicle_rev)

