#  NO USE OF THIS WHEN USING APP.PY

# import torch  
# from file_extractor import extract_text_from_document
# from embedder import generate_embeddings
# from rag import rag_pipeline
# import pandas as pd
# from qdrant_inserting import connect_to_qdrant, create_qdrant_collection,insert_embeddings_to_qdrant
# def main():
    
#     file_path = r"Santhosh_Bio.docx"
    
#     documents = extract_text_from_document(file_path)

#     file_text = [doc.page_content for doc in documents]

#     single_line_text = " ".join(file_text).replace("\n", " ")
    
#     embeddings = generate_embeddings(single_line_text)
    
#     # Ensure embeddings are moved to CPU and converted to list format
#     if isinstance(embeddings, torch.Tensor):
#         embeddings = embeddings.cpu().numpy().tolist()

#     df = pd.DataFrame({
#         'text': [single_line_text],
#         'metadata': [{'title': 'Overview', 'summary': 'A brief summary of Overview'}],
#         'embeddings': [embeddings[0]]
#     })

#     client = connect_to_qdrant()

#     collection_name = "collection"

#     create_qdrant_collection(client, collection_name)

#     insert_embeddings_to_qdrant(df, client, collection_name)
    
#     query_text = "what is santhosh doing currently?"
#     print(f"Query: {query_text}")
#     rag_pipeline(query_text)

# if __name__ == "__main__":
#     main()
