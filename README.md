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

file_extractor(extracts text/content from document) ---> embedder(generates embeddings of the text) ---> Dataframe:main(creating dataframe for the text, metadata and embeddings) ---> qdrant_inserting(connect to qdrant, create collection in qdrant, and insert embeddings into qdrant with df) ---> rag(convert the user query into embedding, perform similarity search on qdrant and getting the text based data, Now passing that text retrieved fromt qdrant and query_text to the openAI client) ---> final response(main.py)

---

## ⚙️ Setup Instructions

### 🔗 Prerequisites

- **Docker** installed and running on your machine
- Pull and run Qdrant using Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant

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
python3 main.py (casual)
streamlit run app.py (streamlit)
