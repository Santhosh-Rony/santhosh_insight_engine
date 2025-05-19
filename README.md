# Santhosh Insight Engine

**Santhosh Insight Engine** is an AI-powered chatbot that allows users to ask natural language questions about Santhosh Chodipilli.  
It uses a custom RAG (Retrieval-Augmented Generation) pipeline to extract, embed, store, and retrieve answers from a document using vector search.

---

## 🚀 Features

- 📄 Automatically indexes and embeds Santhosh's bio (`.docx` file)
- 🤖 Allows natural language queries like:
  - "Where is Santhosh living?"
  - "Where is he working now?"
- ⚙️ Uses Qdrant as the vector database for efficient similarity search
- 🧩 Uses `sentence-transformers` for embedding generation
- 🌐 Interactive web UI built with Streamlit

---

## 🧱 Architecture Overview

Santhosh_Bio.docx
│
▼
[Text Extraction]
file_extractor.py
│
▼
[Generate Embedding]
embedder.py
│
▼
[Store in Vector DB]
qdrant_inserting.py (Qdrant)
│
▼
[app.py]
│
▼
[User Query]
│
▼
[Retrieve Relevant Context]
rag_qdrant.py
│
▼
[Answer Generation]

---

## ⚙️ Setup Instructions

### 🔗 Prerequisites

- **Docker** installed and running on your machine
- Pull and run Qdrant using Docker:

```bash
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
Make sure Qdrant is available at http://localhost:6333 before launching the app.

📦 Install Dependencies
pip install -r requirements.txt

Ensure your requirements.txt contains:
streamlit
torch
pandas
qdrant-client
sentence-transformers
python-docx

▶️ Run the App
streamlit run app.py
