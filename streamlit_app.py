import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langserve import RemoteRunnable
import pandas as pd
import numpy as np


st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_dict = {"hour": list(range(0, 24)), "pickups": np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0].tolist()}
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

instruction = RemoteRunnable("http://localhost:8000/instruction/")

prompt = ChatPromptTemplate.from_template("### Question: Explore the Uber pickups data for New York City, showcasing the number of pickups per hour. The dataset includes hourly counts of pickups throughout the day. Provide insights into the trends and patterns observed in the data. Data: {data}\n ### Answer: ")

chain = prompt | instruction

def generate_response(data):
    st.info(chain.invoke({"data": data}))

generate_response(str(hist_dict))