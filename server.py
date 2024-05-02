from fastapi import FastAPI
from langserve import add_routes
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import pipeline


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")
model.load_adapter("distilgpt2-instruct")
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)
llm = HuggingFacePipeline(pipeline=pipe)
add_routes(
    app,
    llm,
    path="/instruction",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)