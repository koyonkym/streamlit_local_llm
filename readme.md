### English:

# Streamlit and Local Language Model Integration

This project aims to check the integration of Streamlit and a local Language Model (LLM). The source code is based on several tutorial web pages, which are listed below.

## Tutorials Used:
- [Build an LLM app using LangChain](https://docs.streamlit.io/develop/tutorials/llms/llm-quickstart)
- [Quicktour](https://huggingface.co/docs/peft/en/quicktour)
- [Hugging Face Local Pipelines](https://python.langchain.com/docs/integrations/llms/huggingface_pipelines/)
- [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
- [st.scatter_chart](https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart)
- [Sample Application](https://python.langchain.com/docs/langserve/#sample-application)
- [Supervised Fine-tuning Trainer](https://huggingface.co/docs/trl/en/sft_trainer)
- [Datasets:HuggingFaceH4/instruction-dataset](https://huggingface.co/datasets/HuggingFaceH4/instruction-dataset)
- [Causal language modeling](https://huggingface.co/docs/transformers/en/tasks/language_modeling)
- [Load adapters with 🤗 PEFT](https://huggingface.co/docs/transformers/en/peft)

## How to Launch the App:
1. Execute the command `python server.py` to launch the LLM app.
2. Execute the command `streamlit run streamlit_app.py` to launch the Streamlit app.

**Note:** You may need to change the host as needed in deployment, for example, from `localhost` to `0.0.0.0`.

Feel free to explore the code and experiment with Streamlit and your local Language Model!

### Japanese:

# Streamlit と ローカル言語モデルの統合

このプロジェクトは、Streamlit とローカル言語モデル（LLM）の統合を確認することを目的としています。ソースコードはいくつかのチュートリアルウェブページに基づいており、以下にリストされています。

## 使用したチュートリアル:
- [Build an LLM app using LangChain](https://docs.streamlit.io/develop/tutorials/llms/llm-quickstart)
- [Quicktour](https://huggingface.co/docs/peft/en/quicktour)
- [Hugging Face Local Pipelines](https://python.langchain.com/docs/integrations/llms/huggingface_pipelines/)
- [The Iris Dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html)
- [st.scatter_chart](https://docs.streamlit.io/develop/api-reference/charts/st.scatter_chart)
- [Sample Application](https://python.langchain.com/docs/langserve/#sample-application)
- [Supervised Fine-tuning Trainer](https://huggingface.co/docs/trl/en/sft_trainer)
- [Datasets:HuggingFaceH4/instruction-dataset](https://huggingface.co/datasets/HuggingFaceH4/instruction-dataset)
- [Causal language modeling](https://huggingface.co/docs/transformers/en/tasks/language_modeling)
- [Load adapters with 🤗 PEFT](https://huggingface.co/docs/transformers/en/peft)

## アプリの起動方法:
1. `python server.py` を実行して LLM アプリを起動します。
2. `streamlit run streamlit_app.py` を実行して Streamlit アプリを起動します。

**注意:** デプロイ時には必要に応じてホストを変更する必要があります。たとえば、`localhost` から `0.0.0.0` に変更します。

コードを探索して、Streamlit とローカル言語モデルを試してみてください！