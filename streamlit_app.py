import streamlit as st
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer
import torch
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import pipeline
from sklearn import datasets


iris = datasets.load_iris()

model = AutoPeftModelForCausalLM.from_pretrained("ybelkada/opt-350m-lora")
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10)

def generate_response(input_text):
    llm = HuggingFacePipeline(pipeline=pipe)
    st.info(llm(input_text))
    st.scatter_chart(iris.data)

with st.form('my_form'):
    text = 'What are the three key pieces of advice for learning how to code?'
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)