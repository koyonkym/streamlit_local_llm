import streamlit as st
from sklearn import datasets
from langserve import RemoteRunnable


opt = RemoteRunnable("http://localhost:8000/opt/")

iris = datasets.load_iris()

def generate_response(input_text):
    st.info(opt.invoke(input_text))
    st.scatter_chart(iris.data)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)