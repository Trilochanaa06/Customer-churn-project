import streamlit as st
import pandas as pd
import sqlite3

st.title("Customer Churn Analytics Dashboard")

df = pd.read_csv("customers.csv")

st.header("Dataset Overview")
st.write(df.head())

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Churned Customers", df["is_churned"].sum())
col3.metric("Churn Rate", f"{df['is_churned'].mean()*100:.2f}%")

st.header("Subscription Distribution")
st.bar_chart(df["subscription_type"].value_counts())

st.header("Churn by Subscription Type")
churn_by_sub = df.groupby("subscription_type")["is_churned"].mean()
st.bar_chart(churn_by_sub)

st.header("Monthly Spend Distribution")
st.line_chart(df["monthly_spend"])

st.header("High Risk Customers")

high_risk = df[
    (df["days_inactive"] > 30) &
    (df["support_tickets"] > 4)
]

st.write(high_risk)