from sentence_transformers import SentenceTransformer
import json

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load knowledge base
with open("data/knowledge_base.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

# Remove empty lines
documents = [doc.strip() for doc in documents if doc.strip()]

vector_store = []

for idx, text in enumerate(documents):
    embedding = model.encode(text).tolist()

    record = {
        "id": idx,
        "text": text,
        "embedding": embedding
    }

    vector_store.append(record)

# Save vectors locally (simulating vector database storage)
with open("data/vector_store.json", "w", encoding="utf-8") as f:
    json.dump(vector_store, f, indent=4)

print("Data successfully converted into embeddings and stored.")