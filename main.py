import streamlit as st
from langchain.llms.vllm import VLLMOpenAI
from langchain_core.prompts.prompt import PromptTemplate

st.set_page_config(
        page_title="LangChain + vLLM + Streamlit"
        )

st.header("LangChain + vLLM + Streamlit")

system_prompt = st.text_area(
        label="System Prompt",
        value="You are a helpful AI assistant who answers questions in short sentences."
        )

llm = VLLMOpenAI(
        openai_api_key="EMPTY",
        openai_api_base="http://localhost:8000/v1",
        model_name="mistralai/Mistral-7B-Instruct-v0.1"
        )

prompt = PromptTemplate.from_template(
        template="""<s>[INST]{system_prompt}[/INST]
        [INST]{question}[/INST]
        """,
        partial_variables={"system_prompt": system_prompt}
        )

chain = prompt | llm

if "messages" not in st.session_state:
    st.session_state.messages = [
            {"role": "assistant", "content": "How may I help you today?"}
            ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Your message here"):

    st.session_state.messages.append(
            {"role": "human", "content": question}
            )

    with st.chat_message("user"):
        st.markdown(question)

    response = chain.invoke({"question": question})

    st.session_state.messages.append(
            {"role": "assistant", "content": response}
            )

    with st.chat_message("assistant"):
        st.markdown(response)
