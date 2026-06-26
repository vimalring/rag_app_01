import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

# =====================================================
# Load Environment Variables
# =====================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY not found.")
    st.stop()

# =====================================================
# Streamlit Page
# =====================================================

st.set_page_config(
    page_title="RAG Hosting Chat",
    page_icon="📄",
    layout="wide"
)

st.title("📄 RAG Hosting Chat")

st.write(
    "Upload a PDF and ask questions about its content using "
    "Retrieval-Augmented Generation (RAG)."
)

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:
    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type="pdf"
    )

# =====================================================
# Main Logic
# =====================================================

if uploaded_file is None:

    st.info("👈 Upload a PDF to begin.")

else:

    st.success(f"Uploaded: {uploaded_file.name}")

    # ------------------------------------------
    # Save PDF
    # ------------------------------------------

    with st.spinner("📄 Reading PDF..."):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

    # ------------------------------------------
    # Split Text
    # ------------------------------------------

    with st.spinner("✂️ Splitting document..."):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.split_documents(documents)

    # ------------------------------------------
    # Embeddings
    # ------------------------------------------

    with st.spinner("🧠 Creating embeddings..."):

        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    # ------------------------------------------
    # Vector Store
    # ------------------------------------------

    with st.spinner("💾 Building FAISS index..."):

        vector_store = FAISS.from_documents(
            chunks,
            embedding_model
        )

    st.success("✅ Vector Database Ready")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Pages", len(documents))

    with col2:
        st.metric("Chunks", len(chunks))

    # ------------------------------------------
    # Question
    # ------------------------------------------

    st.divider()

    question = st.text_input(
        "💬 Ask a question about the PDF"
    )

    if question:

        with st.spinner("🤖 Generating answer..."):

            retriever = vector_store.as_retriever(
                search_kwargs={"k": 4}
            )

            llm = ChatOpenAI(
                model="gpt-4.1-mini",
                temperature=0
            )

            prompt = ChatPromptTemplate.from_messages(
                [
                    (
                        "system",
                        """You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
say "I couldn't find that information in the PDF."

Context:
{context}
""",
                    ),
                    ("human", "{input}"),
                ]
            )

            document_chain = create_stuff_documents_chain(
                llm,
                prompt
            )

            retrieval_chain = create_retrieval_chain(
                retriever,
                document_chain
            )

            response = retrieval_chain.invoke(
                {
                    "input": question
                }
            )

        st.subheader("🤖 Answer")

        st.write(response["answer"])