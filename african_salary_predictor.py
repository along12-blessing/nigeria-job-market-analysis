import pandas as pd
import streamlit as st

st.title("Nigeria Job Market Dashboard")

df = pd.read_csv("Nigeria_job_market.csv", index_col=0)

st.subheader("Full Dataset")
st.dataframe(df.reset_index(drop=True))

avg_salary = df.groupby('Industry')['Salary'].mean()

st.subheader("Filter by City")
city = st.sidebar.selectbox("Select your city", ["Lagos", "Abuja", "Port Harcourt", "Kano", "Ibadan"])

st.write(f"You selected {city}")

filtered_df = df[df['City'] == city]

industry_filter = st.sidebar.selectbox("Select Industry", ["All", "Tech", "Finance", "Oil & Gas", "Education", "Healthcare"])

st.subheader("Average Salary by Industry")
st.dataframe(filtered_df.reset_index(drop=True))
st.bar_chart(avg_salary)

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

x = pd.get_dummies(df[['Industry']])
x['Years_Experience'] = df['Years_Experience']

y = df['Salary']

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(x_train,y_train)

years_experience = st.text_input("Enter Years of experience")
industry = st.selectbox("Select Industry", ["Tech", "Finance", "Oil & Gas", "Healthcare"])

if st.button("Predict salary"):
    input_data = pd.DataFrame(columns=x.columns)  # create empty row with same columns
    input_data.loc[0] = 0                          # fill everything with 0
    input_data[f'Industry_{industry}'] = 1         # set chosen industry to 1
    input_data['Years_Experience'] = int(years_experience)  # set experience
    
    prediction = model.predict(input_data)
    st.write(f"Predicted Salary: ₦{prediction[0]:,.2f}")

user_input = st.text_input("Enter word")    

if 'messages' not in st.session_state:
    st.session_state.messages = []
    
if st.button("Click"):
    st.session_state.messages.append(user_input)
    
for message in st.session_state.messages:
    st.write(message)
    
upload_file = st.file_uploader("Upload your file",type="csv")


if upload_file is not None:
    df = pd.read_csv(upload_file, index_col=0)
    st.dataframe(df.reset_index(drop=True))