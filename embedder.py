from sentence_transformers import SentenceTransformer

def generate_embeddings(texts):

    model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu") 

    # Removing empty strings from the texts list
    texts = [text for text in texts if text.strip()]

    embeddings = model.encode(texts, convert_to_tensor=True)
    return embeddings
