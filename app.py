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
    page_title="Santhosh Insight Engine",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data(show_spinner=False)
def index_document():
    with open("Santhosh_Bio.docx", "rb") as dfp:
        content = dfp.read()
    with open("indexed_doc.docx", "wb") as tmp:
        tmp.write(content)
    documents = extract_text_from_document("indexed_doc.docx")
    file_text = " ".join(doc.page_content for doc in documents).replace("\n", " ")
    embeddings = generate_embeddings(file_text)
    if isinstance(embeddings, torch.Tensor):
        embeddings = embeddings.cpu().numpy().tolist()
    df = pd.DataFrame({
        'text': [file_text],
        'metadata': [{'title': 'Overview', 'summary': 'A brief summary of Overview'}],
        'embeddings': [embeddings[0]]
    })
    client = connect_to_qdrant()
    create_qdrant_collection(client, "collection")
    insert_embeddings_to_qdrant(df, client, "collection")
    return True

index_document()

# Custom CSS for futuristic UI
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    html, body, [class*="css"]  {
      background-color: #0a0a0a;
      color: #e0e0e0;
      font-family: 'Orbitron', sans-serif;
    }
    .title {
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
      background: linear-gradient(90deg, #00d4ff, #0066ff);
      border: none;
      border-radius: 12px;
      box-shadow: 0 0 8px rgba(0, 212, 255, 0.7), 0 0 16px rgba(0, 102, 255, 0.7);
      color: #ffffff;
      height: 48px;
      width: 100%;
      font-size: 18px;
      font-weight: 700;
      cursor: pointer;
      transition: box-shadow 0.3s ease;
    }
    .stButton>button:hover {
      box-shadow: 0 0 12px rgba(0, 212, 255, 1), 0 0 24px rgba(0, 102, 255, 1);
    }
    .stTextInput>div>div>input {
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
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main interface
st.markdown("<div class='title'>🚀 Santhosh Insight Engine</div>", unsafe_allow_html=True)
st.markdown("---")

# Input section
query = st.text_input("Ask about Santhosh", placeholder="e.g. Where is Santhosh working now?")
get_answer = st.button("Get Answer")

# Response section
if get_answer and query:
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

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#555555'>Built by Santhosh__rony</p>", unsafe_allow_html=True)
