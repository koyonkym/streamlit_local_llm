from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from transformers import pipeline
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
import logging
import os
import sys


model = AutoModelForCausalLM.from_pretrained("distilbert/distilgpt2")
model.load_adapter("distilgpt2-instruct")
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilgpt2")
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=100)


SERVICE_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
SERVER_PORT = os.getenv('SERVER_PORT', 8080)


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(
        logging.Formatter(
            '%(name)s [%(asctime)s] [%(levelname)s] %(message)s'))
    logger.addHandler(handler)
    return logger


logger = get_logger('llm-service')

app = Flask(__name__)


@app.get("/healthcheck")
def readiness_probe():
    return "I'm ready!"


@app.post("/instruction")
def instruction():
    '''
    Main handler for input data sent by Snowflake.
    '''
    message = request.json
    logger.debug(f'Received request: {message}')

    if message is None or not message['data']:
        logger.info('Received empty message')
        return {}

    # input format:
    #   {"data": [
    #     [row_index, column_1_value, column_2_value, ...],
    #     ...
    #   ]}
    input_rows = message['data']
    logger.info(f'Received {len(input_rows)} rows')

    # output format:
    #   {"data": [
    #     [row_index, column_1_value, column_2_value, ...}],
    #     ...
    #   ]}
    output_rows = [[row[0], get_llm_response(row[1])] for row in input_rows]
    logger.info(f'Produced {len(output_rows)} rows')

    response = make_response({"data": output_rows})
    response.headers['Content-type'] = 'application/json'
    logger.debug(f'Sending response: {response.json}')
    return response


@app.route("/ui", methods=["GET", "POST"])
def ui():
    '''
    Main handler for providing a web UI.
    '''
    if request.method == "POST":
        # getting input in HTML form
        input_text = request.form.get("input")
        # display input and output
        return render_template("basic_ui.html",
            llm_input=input_text,
            llm_reponse=get_llm_response(input_text))
    return render_template("basic_ui.html")


def get_llm_response(input):
    return pipe(input, return_full_text=False)[0]['generated_text']

if __name__ == '__main__':
    app.run(host=SERVICE_HOST, port=SERVER_PORT)