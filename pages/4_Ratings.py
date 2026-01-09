import streamlit as st
import pandas as pd

@st.cache_data
def load():
    return pd.read_csv("OLA_DataSet_CLEANED.csv")

df = load()

st.title("⭐ Ratings")

cust = df.groupby("Vehicle_Type")["Customer_Rating"].mean()
driver = df.groupby("Vehicle_Type")["Driver_Ratings"].mean()

st.subheader("Customer Ratings by Vehicle")
st.bar_chart(cust)

st.subheader("Driver Ratings by Vehicle")
st.bar_chart(driver)

