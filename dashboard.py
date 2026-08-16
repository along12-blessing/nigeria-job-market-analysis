import pandas as pd
import streamlit as st

st.title("Nigeria Job Market Dashboard")

df = pd.read_csv("Nigeria_job_market.csv", index_col=0)

st.subheader("Full Dataset")
st.dataframe(df.reset_index(drop=True))

avg_salary = df.groupby('Industry')['Salary'].mean()

st.subheader("Filter by City")
city = st.selectbox("Select your city", ["Lagos", "Abuja", "Port Harcourt", "Kano", "Ibadan"])
st.write(f"You selected {city}")

filtered_df = df[df['City'] == city]

st.subheader("Average Salary by Industry")
st.dataframe(filtered_df.reset_index(drop=True))
st.bar_chart(avg_salary)