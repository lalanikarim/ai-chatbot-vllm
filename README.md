---
title: Ai Chatbot w/ Langchain, vLLM, and Streamlit
emoji: 📊
colorFrom: indigo
colorTo: gray
sdk: streamlit
sdk_version: 1.28.0
app_file: main.py
pinned: false
license: mit
---

# Streamlit + Langchain + vLLM w/ Mistral

Run your own AI Chatbot locally on a GPU or even a CPU.

To make that possible, we use the [Mistral 7b](https://mistral.ai/news/announcing-mistral-7b/) model.  
We will use an LLM Inference engine called [vLLM](https://vllm.ai) to serve an OpenAI compatible API  
and run our LLM there and have LangChain connect to it instead of running it directly.

This AI chatbot will allow you to define its personality and respond to the questions accordingly.  
There is no chat memory in this iteration, so you won't be able to ask follow-up questions.
The chatbot will essentially behave like a Question/Answer bot.

# TL;DR instructions

1. Install vllm
2. Install langchain
3. Install streamlit
4. Start vllm
5. Run streamlit

# Step by Step instructions

The setup assumes you have `python` already installed and `venv` module available.

1. Install `vllm` from [vllm.ai](https://docs.vllm.ai/en/latest/).
2. Download the code or clone the repository.
3. Inside the root folder of the repository, initialize a python virtual environment:
```bash
python -m venv .venv
```
4. Activate the python environment:
```bash
source .venv/bin/activate
```
5. Install required packages (`langchain`, `vllm`, `openai`, and `streamlit`):
```bash
pip install -r requirements.txt
```
6. Start `vllm` OpenAI compatible api server:
```bash
python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.1
```
7. Start `streamlit`:
```bash
streamlit run main.py
```

