import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ola Ride Insights", page_icon="🚗", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("OLA_DataSet_CLEANED.csv")
    df["Booking_Datetime"] = pd.to_datetime(df["Booking_Datetime"], errors="coerce")
    return df

df = load_data()

st.title("🚗 Ola Ride Insights – Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Rides", len(df))
col2.metric("Completed", df["Booking_Status"].str.contains("Success", na=False).sum())
col3.metric("Cancelled", df["Booking_Status"].str.contains("Customer|Driver", na=False).sum())
col4.metric("Revenue", f"₹ {df[df['Booking_Status'].str.contains('Success',na=False)]['Booking_Value'].sum():,.0f}")
col5.metric("Avg Rating", round(df["Customer_Rating"].mean(),2))

st.markdown("### Dataset Preview")
st.dataframe(df.head(50))




