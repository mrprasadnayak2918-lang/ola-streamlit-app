
import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(
    page_title="Ola Ride Insights",
    page_icon="🚗",
    layout="wide"
)

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("🚗 Ola Ride Insights – Overview")
st.markdown("Business snapshot of ride operations")

kpi = fetch_data("""
SELECT
    COUNT(*) AS total_rides,
    SUM(CASE WHEN booking_status LIKE '%Success%' THEN 1 ELSE 0 END) AS completed,
    SUM(CASE WHEN booking_status LIKE '%Customer%' OR booking_status LIKE '%Driver%' THEN 1 ELSE 0 END) AS cancelled,
    SUM(CASE WHEN booking_status LIKE '%Success%' THEN booking_value ELSE 0 END) AS revenue,
    ROUND(AVG(customer_rating),2) AS avg_rating
FROM ola_dataset_cleaned
""")

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("🚗 Total Rides", int(kpi.total_rides[0]))
c2.metric("✅ Completed", int(kpi.completed[0]))
c3.metric("❌ Cancelled", int(kpi.cancelled[0]))
c4.metric("💰 Revenue", f"₹ {round(kpi.revenue[0],2)}")
c5.metric("⭐ Avg Rating", kpi.avg_rating[0])

import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(layout="wide")

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("📈 Ride Trends")

df = fetch_data("""
SELECT DATE(booking_datetime) AS ride_date,
       COUNT(*) AS total_rides
FROM ola_dataset_cleaned
GROUP BY ride_date
ORDER BY ride_date
""")

st.line_chart(df.set_index("ride_date"))

import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(layout="wide")

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("💰 Revenue Insights")

df = fetch_data("""
SELECT payment_method,
       SUM(booking_value) AS revenue
FROM ola_dataset_cleaned
WHERE booking_status LIKE '%Success%'
GROUP BY payment_method
ORDER BY revenue DESC
""")

st.bar_chart(df.set_index("payment_method"))

import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(layout="wide")

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("❌ Cancellation Analysis")

df = fetch_data("""
SELECT COALESCE(cancellation_reason_customer,'Unknown') AS reason,
       COUNT(*) AS total
FROM ola_dataset_cleaned
WHERE booking_status LIKE '%Customer%'
GROUP BY reason
ORDER BY total DESC
""")

st.bar_chart(df.set_index("reason"))

import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(layout="wide")

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )

def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

st.title("⭐ Ratings Analysis")

df = fetch_data("""
SELECT vehicle_type,
       ROUND(AVG(customer_rating),2) AS avg_rating
FROM ola_dataset_cleaned
GROUP BY vehicle_type
""")

st.bar_chart(df.set_index("vehicle_type"))

