### English:

# Streamlit and Local Large Language Model Integration

This project aims to check the integration of Streamlit and a local Large Language Model (LLM). The source code is based on several tutorial web pages, which are listed below.

## Tutorials Used:
- [Build an LLM app using LangChain - Streamlit Docs](https://docs.streamlit.io/develop/tutorials/llms/llm-quickstart)
- [Quicktour](https://huggingface.co/docs/peft/en/quicktour)
- [Supervised Fine-tuning Trainer](https://huggingface.co/docs/trl/en/sft_trainer)
- [HuggingFaceH4/instruction-dataset · Datasets at Hugging Face](https://huggingface.co/datasets/HuggingFaceH4/instruction-dataset)
- [Causal language modeling](https://huggingface.co/docs/transformers/en/tasks/language_modeling)
- [Load adapters with 🤗 PEFT](https://huggingface.co/docs/transformers/en/peft)
- [Create an app - Streamlit Docs](https://docs.streamlit.io/get-started/tutorials/create-an-app)
- [st.warning - Streamlit Docs](https://docs.streamlit.io/develop/api-reference/status/st.warning)
- [Tutorial 1: Create a Snowpark Container Services Service | Snowflake Documentation](https://docs.snowflake.com/en/developer-guide/snowpark-container-services/tutorials/tutorial-1)
- [Pipelines](https://huggingface.co/docs/transformers/v4.40.1/en/main_classes/pipelines#transformers.TextGenerationPipeline)

## How to Launch the App:
1. Execute the command `python server.py` to launch the LLM app.
2. Execute the command `streamlit run streamlit_app.py` to launch the Streamlit app.

**Note:** You may need to change the host as needed in deployment, for example, from `localhost` to `0.0.0.0`.

**Instructions to Run `sft_lora.py` in Google Colab or Kaggle Notebook:**
1. `!git clone https://github.com/koyonkym/streamlit_local_llm.git`
2. `!pip install -r streamlit_local_llm/requirements.txt`
3. Execute `!wandb disabled` if you use Kaggle notebook.
4. Execute `!python streamlit_local_llm/sft_lora.py`
5. Execute `!zip -r distilgpt2-instruct.zip distilgpt2-instruct`.
6. Execute the following if you use Google Colab: 
    ```python
    from google.colab import files
    files.download("distilgpt2-instruct.zip")
    ```

Feel free to explore the code and experiment with Streamlit and your local Language Model!

### Japanese:

# Streamlit と ローカル大規模言語モデルの統合

このプロジェクトは、Streamlit とローカル大規模言語モデル（LLM）の統合を確認することを目的としています。ソースコードはいくつかのチュートリアルウェブページに基づいており、以下にリストされています。

## 使用したチュートリアル:
- [Build an LLM app using LangChain - Streamlit Docs](https://docs.streamlit.io/develop/tutorials/llms/llm-quickstart)
- [Quicktour](https://huggingface.co/docs/peft/en/quicktour)
- [Supervised Fine-tuning Trainer](https://huggingface.co/docs/trl/en/sft_trainer)
- [HuggingFaceH4/instruction-dataset · Datasets at Hugging Face](https://huggingface.co/datasets/HuggingFaceH4/instruction-dataset)
- [Causal language modeling](https://huggingface.co/docs/transformers/en/tasks/language_modeling)
- [Load adapters with 🤗 PEFT](https://huggingface.co/docs/transformers/en/peft)
- [Create an app - Streamlit Docs](https://docs.streamlit.io/get-started/tutorials/create-an-app)
- [st.warning - Streamlit Docs](https://docs.streamlit.io/develop/api-reference/status/st.warning)
- [Tutorial 1: Create a Snowpark Container Services Service | Snowflake Documentation](https://docs.snowflake.com/ja/developer-guide/snowpark-container-services/tutorials/tutorial-1)
- [Pipelines](https://huggingface.co/docs/transformers/v4.40.1/en/main_classes/pipelines#transformers.TextGenerationPipeline)

## アプリの起動方法:
1. `python server.py` を実行して LLM アプリを起動します。
2. `streamlit run streamlit_app.py` を実行して Streamlit アプリを起動します。

**注意:** デプロイ時には必要に応じてホストを変更する必要があります。たとえば、`localhost` から `0.0.0.0` に変更します。

**Google Colab や Kaggle Notebook で `sft_lora.py` を実行する手順:**
1. `!git clone https://github.com/koyonkym/streamlit_local_llm.git`
2. `!pip install -r streamlit_local_llm/requirements.txt`
3. Kaggle Notebook を使用する場合は `!wandb disabled` を実行してください。
4. `!python streamlit_local_llm/sft_lora.py` を実行します。
5. `!zip -r distilgpt2-instruct.zip distilgpt2-instruct` を実行します。
6. Google Colab を使用する場合は、以下を実行してください:
    ```python
    from google.colab import files
    files.download("distilgpt2-instruct.zip")
    ```

コードを探索して、Streamlit とローカル言語モデルを試してみてください！