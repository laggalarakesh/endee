import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load vector store
with open("data/vector_store.json", "r", encoding="utf-8") as f:
    vector_store = json.load(f)

query = input("Enter your search query: ")

query_embedding = model.encode(query).reshape(1, -1)

scores = []

for record in vector_store:
    doc_embedding = [record["embedding"]]
    similarity = cosine_similarity(query_embedding, doc_embedding)[0][0]

    scores.append((similarity, record["text"]))

scores.sort(reverse=True)

print("\nTop Results:\n")

for score, text in scores[:3]:
    print(f"{score:.3f} → {text}")