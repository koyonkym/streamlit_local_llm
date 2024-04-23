from fastapi import FastAPI
from langserve import add_routes
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer
import torch
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import pipeline


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

model = AutoPeftModelForCausalLM.from_pretrained("ybelkada/opt-350m-lora")
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-350m")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10)
llm = HuggingFacePipeline(pipeline=pipe)
add_routes(
    app,
    llm,
    path="/opt",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)