from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from generate_response_qdrant import generate_response_from_qdrant
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

model = SentenceTransformer("all-MiniLM-L6-v2")

def query_embeddings_from_qdrant(query_text):
    try:
        
        client = QdrantClient(host="localhost", port=6333)  
        collection_name = "collection"

        # Generating query embeddings 
        query_embedding = model.encode(query_text).tolist()

        # Performing the similarity search on Qdrant
        search_results = client.search(
            collection_name=collection_name,
            query_vector=query_embedding,  # Passing query embedding as vector to search
            limit=10 
        )
        
        if search_results:
            
            retrieved_texts = [result.payload["text"] for result in search_results]
            
            generate_response_from_qdrant(query_text, retrieved_texts)
    
            return retrieved_texts
        else:
            print("No results found.")
            return 

    except Exception as e:
        print(f"Error querying Qdrant: {e}")
        return 
