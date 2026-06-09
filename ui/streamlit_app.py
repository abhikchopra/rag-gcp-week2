import streamlit as st

from app.rag_pipeline import build_index
from app.qa import ask_question

st.set_page_config(page_title="RAG Chatbot", layout="wide")

st.title("📄 Multi-Document RAG Chatbot")

@st.cache_resource
def load_store():
    return build_index("data/pdfs")

store = load_store()

st.success("Index loaded successfully!")

question = st.text_input("Ask a question about your documents")

if question:
    with st.spinner("Thinking..."):
        answer = ask_question(store, question)

    st.markdown("### Answer")
    st.write(answer)