import streamlit as st

from rag_pipeline import build_index
from qa import ask_question


@st.cache_resource
def load_store():
    return build_index("data/sample.pdf")


store = load_store()

st.title("📄 PDF Chatbot")

question = st.text_input("Ask a question about your PDF")

if question:
    with st.spinner("Thinking..."):
        answer = ask_question(store, question)

    st.write("### Answer")
    st.write(answer)