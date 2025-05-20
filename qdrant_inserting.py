from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams

def connect_to_qdrant():
    client = QdrantClient(host="localhost", port=6333)  
    return client

def create_qdrant_collection(client, collection_name):

    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)  # 384-dimensional vectors
    )

# Insert Data into Qdrant Collection
def insert_embeddings_to_qdrant(df, client, collection_name):

    points = [
        PointStruct(
            id=i,
            vector=row['embeddings'],
            payload={
                "text": row['text'],
                "metadata": row['metadata']
            }
        )
        for i, row in df.iterrows()
    ]
    
    # Insert points
    client.upsert(collection_name=collection_name, points=points)
    