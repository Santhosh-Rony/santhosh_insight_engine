from query_qdrant_embeddings import query_embeddings_from_qdrant

def rag_pipeline(query_text):
    try:
        query_embeddings_from_qdrant(query_text)

    except Exception as e:
        print(f"Error in RAG pipeline: {e}")
        return "I'm sorry, I couldn't generate a response at this time."
