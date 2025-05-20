import streamlit as st
import torch
import pandas as pd
import io
import sys
from file_extractor import extract_text_from_document
from embedder import generate_embeddings
from rag import rag_pipeline
from qdrant_inserting import connect_to_qdrant, create_qdrant_collection, insert_embeddings_to_qdrant

st.set_page_config(
    page_title="AskMyDoc AI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Audiowide&family=Roboto:wght@400;500;700&display=swap');

    html, body, [class*="css"]  {
      background-color: #0a0a0a;
      color: #e0e0e0;
      font-family: 'Roboto', sans-serif;
    }
    .title {
      font-family: 'Audiowide', cursive;
      font-size: 60px;
      font-weight: 700;
      text-align: center;
      margin-top: 20px;
      background: linear-gradient(90deg, #00ffea, #0070ff, #00ffea);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      animation: neonGlow 2s ease-in-out infinite alternate;
    }
    @keyframes neonGlow {
      from { text-shadow: 0 0 10px #00ffea, 0 0 20px #00ffea; }
      to { text-shadow: 0 0 20px #0070ff, 0 0 30px #0070ff; }
    }
    .stButton>button {
      font-family: 'Roboto', sans-serif;
      background: linear-gradient(90deg, #00d4ff, #0066ff);
      border: none;
      border-radius: 12px;
      box-shadow: 0 0 8px rgba(0, 212, 255, 0.7), 0 0 16px rgba(0, 102, 255, 0.7);
      color: #ffffff;
      height: 48px;
      width: 100%;
      font-size: 18px;
      font-weight: 500;
      cursor: pointer;
      transition: box-shadow 0.3s ease;
    }
    .stButton>button:hover {
      box-shadow: 0 0 12px rgba(0, 212, 255, 1), 0 0 24px rgba(0, 102, 255, 1);
    }
    .stTextInput>div>div>input {
      font-family: 'Roboto', sans-serif;
      background-color: #1e1e1e;
      border: 1px solid #333333;
      border-radius: 8px;
      color: #e0e0e0;
      padding: 12px;
      font-size: 16px;
    }
    .response-card {
      background-color: #1f1f1f;
      border-left: 4px solid #00d4ff;
      border-radius: 8px;
      padding: 20px;
      margin-top: 20px;
      animation: fadeIn 0.5s ease-in-out;
    }
    .response-card h4, .response-card p {
      font-family: 'Roboto', sans-serif;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>🚀 AskMyDoc AI</div>", unsafe_allow_html=True)
st.markdown("---")

uploaded_file = st.file_uploader(
    label="Upload your document",
    type=["pdf", "docx", "txt"],
    help="Supported formats: PDF, DOCX, TXT"
)

def process_and_index(file_bytes, filename):
    tmp_path = f"uploaded_{filename}"
    with open(tmp_path, "wb") as f:
        f.write(file_bytes)
    documents = extract_text_from_document(tmp_path)
    file_text = " ".join(doc.page_content for doc in documents).replace("\n", " ")
    embeddings = generate_embeddings(file_text)
    if isinstance(embeddings, torch.Tensor):
        embeddings = embeddings.cpu().numpy().tolist()
    df = pd.DataFrame({
        'text': [file_text],
        'metadata': [{'title': filename, 'summary': ''}],
        'embeddings': [embeddings[0]]
    })
    client = connect_to_qdrant()
    try:
        client.delete_collection("collection")
    except Exception:
        pass
    create_qdrant_collection(client, "collection")
    insert_embeddings_to_qdrant(df, client, "collection")

if uploaded_file:
    st.success(f"File '{uploaded_file.name}' uploaded and indexed.")
    file_bytes = uploaded_file.getvalue()
    process_and_index(file_bytes, uploaded_file.name)
    query = st.text_input("Ask anything about the uploaded document:")
    if st.button("Get Answer") and query:
        st.markdown("<div class='response-card'>", unsafe_allow_html=True)
        st.markdown(f"<p>Question:</p><p>{query}</p>", unsafe_allow_html=True)
        with st.spinner("Processing your question..."):
            buf = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = buf
            result = rag_pipeline(query)
            sys.stdout = old_stdout
            answer = result if result else buf.getvalue().strip()
            if not answer:
                answer = "No answer returned. Check your RAG pipeline implementation."
        st.markdown(f"<p>{answer}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center; color:#555555; font-family: Roboto, sans-serif;'>Built by Santhosh__rony</p>", unsafe_allow_html=True)
