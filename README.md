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

```bash 
file_extractor(extracts text/content from document) ---> embedder(generates embeddings of the text) ---> Dataframe:main(creating dataframe for the text, metadata and embeddings) ---> qdrant_inserting(connect to qdrant, create collection in qdrant, and insert embeddings into qdrant with df) ---> rag(convert the user query into embedding, perform similarity search on qdrant and getting the text based data, Now passing that text retrieved fromt qdrant and query_text to the openAI client) ---> final response(main.py)
```
---

## ⚙️ Setup Instructions

### 🔗 Prerequisites

- **Docker** installed and running on your machine
- Pull and run Qdrant using Docker:

```bash 
1--> Pull 2--> Only using HTTP API 3--> Using both HTTP and gRPC APIs (choose explictly)
docker pull qdrant/qdrant
docker run -p 6333:6333 qdrant/
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant  


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
```

## Repository Overview

This repository contains three distinct implementations of a document-based QA engine. Each lives in its own Git branch:

| Branch       | Title                         | Description                                                                  |
| ------------ | ----------------------------- | ---------------------------------------------------------------------------- |
| `python`     | Santhosh Insight Engine (CLI) | A command-line Python module for querying Santhosh's biography.              |
| `streamlit`  | Santhosh Insight Engine (App) | A Streamlit web app providing an interactive UI for the same.                |
| `upload-doc` | AskMyDoc AI                   | A general-purpose uploader: users can upload any document and ask questions. |

---

## 1. `python` Branch: Santhosh Insight Engine (CLI)

**Purpose**: A lightweight Python script for querying a hard‑coded Santhosh biography.

### Setup & Run

```bash
# 1. Clone this repository
git clone https://github.com/Santhosh-Rony/santhosh_insight_engine.git
cd santhosh_insight_engine

# 2. Switch to python branch
git checkout python

# 3. Create virtual environment & install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 4. Run the CLI query script
python santhosh_insight.py --question "Where is Santhosh working now?"
```

### Notes

* The bio file `Santhosh_Bio.docx` is tracked in this branch.
* All embeddings & RAG logic is pre‑configured for that single document.

---

## 2. `streamlit` Branch: Santhosh Insight Engine (App)

**Purpose**: A full-featured Streamlit application with custom futuristic UI.

### Setup & Run

```bash
# 1. Switch to streamlit branch
git checkout streamlit

# 2. (If not already) activate your virtual environment
source .venv/bin/activate

# 3. Install/update dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
```

### Features

* Animated neon title and dark-mode styling
* Hard‑coded indexing of `Santhosh_Bio.docx` on startup
* Input field and question/answer cards in a single-page layout

---

## 3. `upload-doc` Branch: AskMyDoc AI

**Purpose**: A branching extension that allows **any user** to upload a PDF/DOCX/TXT file and ask questions about it.

### Setup & Run

```bash
# 1. Switch to upload-doc branch
git checkout upload-doc

# 2. Activate environment & install
source .venv/bin/activate
pip install -r requirements.txt

# 3. Launch the Streamlit uploader app
streamlit run app.py
```

### Usage

1. Upload a supported file via the uploader widget.
2. Wait for automatic indexing and embedding.
3. Enter your query in the text box and click **Get Answer**.

---

## Common Requirements

* Python 3.8+ (tested on 3.10.12)
* Docker & Qdrant server running (if you are using the Qdrant-backed vector store)
* Access to internet for loading Transformer models

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add YourFeature"`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

#### Note : You must have your own 'OpenAI API key'

## License

This project is MIT licensed. See [LICENSE](LICENSE) for details.

