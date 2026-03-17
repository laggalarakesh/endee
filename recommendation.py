import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load vector database
with open("data/vector_store.json", "r", encoding="utf-8") as f:
    vector_store = json.load(f)


def recommend(topic, top_k=3):

    topic_embedding = model.encode(topic).reshape(1, -1)

    scores = []

    for record in vector_store:

        doc_embedding = [record["embedding"]]

        similarity = cosine_similarity(topic_embedding, doc_embedding)[0][0]

        scores.append((similarity, record["text"]))

    scores.sort(reverse=True)

    recommendations = [text for _, text in scores[:top_k]]

    return recommendations


if __name__ == "__main__":

    topic = input("Enter a topic to get recommendations: ")

    recs = recommend(topic)

    print("\nRecommended Topics:\n")

    for r in recs:
        print("-", r)