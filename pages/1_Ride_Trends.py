import streamlit as st
import pandas as pd

@st.cache_data
def load():
    df = pd.read_csv("OLA_DataSet_CLEANED.csv")
    df["Booking_Datetime"] = pd.to_datetime(df["Booking_Datetime"], errors="coerce")
    return df

df = load()

st.title("📈 Ride Trends")

trend = df.groupby(df["Booking_Datetime"].dt.date).size()
st.line_chart(trend)

vehicle = df["Vehicle_Type"].value_counts()
st.bar_chart(vehicle)

