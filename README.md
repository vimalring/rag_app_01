# 📄 RAG PDF Chat Application

A Retrieval-Augmented Generation (RAG) application built with **Python, Streamlit, LangChain, Hugging Face Embeddings, FAISS, and OpenAI**. Users can upload a PDF document and ask natural language questions, with answers generated from the uploaded document.

---

## 🚀 Project Overview

This project demonstrates how to build a simple Retrieval-Augmented Generation (RAG) application using LangChain.

The application allows users to:

* Upload a PDF document
* Extract and split the document into chunks
* Generate embeddings using a Hugging Face model
* Store embeddings in a FAISS vector database
* Ask questions about the uploaded PDF
* Retrieve relevant document chunks
* Generate grounded answers using OpenAI GPT

---

## 🛠 Tech Stack

* Python 3.12
* Streamlit
* LangChain
* Hugging Face Embeddings
* FAISS Vector Database
* OpenAI GPT
* PyPDF
* LangSmith (Optional)

---

## 📂 Project Structure

```
rag-app/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── venv/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rag-pdf-chat.git
cd rag-pdf-chat
```

---

### 2. Create Virtual Environment

macOS / Linux

```bash
python3.12 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install \
streamlit \
langchain \
langchain-community \
langchain-openai \
langchain-huggingface \
langchain-text-splitters \
langchain-classic \
sentence-transformers \
faiss-cpu \
pypdf \
python-dotenv \
langsmith
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```
OPENAI_API_KEY=your_openai_api_key
```

Replace:

```
your_openai_api_key
```

with your actual OpenAI API Key.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

Default URL:

```
http://localhost:8501
```

---

## 🧠 RAG Workflow

```
User Uploads PDF
        │
        ▼
Read PDF
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
(Hugging Face)
        │
        ▼
Store in FAISS
        │
        ▼
User Question
        │
        ▼
Similarity Search
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
OpenAI GPT
        │
        ▼
Final Answer
```

---

## 📚 Features

* PDF Upload
* PDF Text Extraction
* Intelligent Text Chunking
* Hugging Face Embeddings
* FAISS Vector Search
* OpenAI GPT Response Generation
* Streamlit User Interface
* Environment Variable Support
* Local Vector Database

---

## 📦 Python Packages

* streamlit
* langchain
* langchain-community
* langchain-openai
* langchain-huggingface
* langchain-text-splitters
* langchain-classic
* sentence-transformers
* faiss-cpu
* pypdf
* python-dotenv
* langsmith

---

## 💡 Example Usage

### Upload

```
Artificial_Intelligence.pdf
```

### Ask

```
What are the key findings?
```

### Response

```
The document highlights three key findings...

1. ...
2. ...
3. ...
```

---

## 📸 Screenshots

Add screenshots here after running the application.

Example:

```
screenshots/

├── home.png
├── upload.png
├── vector-db.png
└── answer.png
```

---

## 📖 Learning Objectives

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Document Processing
* Semantic Search
* Vector Databases
* Embeddings
* Prompt Engineering
* LangChain Workflows
* Streamlit Application Development

---

## 🚧 Future Improvements

* Multiple PDF Support
* Chat History
* Source Document References
* Persistent FAISS Database
* Streaming Responses
* Citation Support
* LangSmith Tracing
* Docker Support
* Deployment on Streamlit Cloud

---

## 👨‍💻 Author

**VIMAL**



## 📄 License

This project is developed for educational purposes as part of the **Gen AI Architect Program – Assignment 6**.

Feel free to fork, learn, and improve upon it.

---

## ⭐ If you found this project helpful

Please consider giving the repository a ⭐ on GitHub.
