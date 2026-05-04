import streamlit as st
import pandas as pd
from analysis import analyze_data

st.title("RetailRevive – Store Performance Optimization")

# Load data
df = pd.read_csv("data.csv")

st.subheader("Store Data")
st.dataframe(df)

# Analyze
df, underperforming, insights = analyze_data(df)

st.subheader("Analysis Results")
st.dataframe(df)

st.subheader("Underperforming Stores")
st.dataframe(underperforming)

st.subheader("Insights")
for i in insights:
    st.write("- " + i)
