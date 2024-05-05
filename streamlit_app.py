import streamlit as st
import pandas as pd
import numpy as np
import requests


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

prompt = f"### Question: Explore the Uber pickups data for New York City, showcasing the number of pickups per hour. The dataset includes hourly counts of pickups throughout the day. Provide insights into the trends and patterns observed in the data. Data: {str(hist_dict)}\n ### Answer: "

def generate_response(prompt):
    url = 'http://localhost:8080/instruction'
    input_rows = [[0, prompt]]
    data = {
        'data': input_rows,
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print('Error:', response.status_code)
    message = response.json()
    st.info(message['data'][0][1])
    st.warning("This project focuses solely on verifying the integration between Streamlit and the local Large Language Model (LLM). Please note that generated texts may lack coherence or relevance.", icon="⚠️")

generate_response(prompt)