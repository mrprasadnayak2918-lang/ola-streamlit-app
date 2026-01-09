
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Ola Ride Insights",
    page_icon="🚗",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("OLA_DataSet_CLEANED.csv")
    df["Booking_Datetime"] = pd.to_datetime(df["Booking_Datetime"], errors="coerce")
    return df

df = load_data()

st.title("🚗 Ola Ride Insights – Overview")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("🚗 Total Rides", len(df))
col2.metric("✅ Completed Rides", df["Booking_Status"].str.contains("Success", na=False).sum())
col3.metric("❌ Cancelled Rides", df["Booking_Status"].str.contains("Customer|Driver", na=False).sum())
col4.metric(
    "💰 Revenue",
    f"₹ {df.loc[df['Booking_Status'].str.contains('Success', na=False), 'Booking_Value'].sum():,.2f}"
)
col5.metric("⭐ Avg Rating", round(df["Customer_Rating"].mean(), 2))

st.markdown("---")

st.subheader("📈 Ride Trends")
trend = df.groupby(df["Booking_Datetime"].dt.date).size()
st.line_chart(trend)

st.subheader("💳 Revenue by Payment Method")
revenue = df[df["Booking_Status"].str.contains("Success", na=False)] \
            .groupby("Payment_Method")["Booking_Value"].sum()
st.bar_chart(revenue)

st.subheader("❌ Customer Cancellation Reasons")
cancel = df[df["Booking_Status"].str.contains("Customer", na=False)] \
            ["Cancellation_Reason_Customer"].fillna("Unknown").value_counts()
st.bar_chart(cancel)


