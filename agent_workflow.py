from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load vector store
with open("data/vector_store.json", "r", encoding="utf-8") as f:
    vector_store = json.load(f)


def search_documents(query, top_k=3):

    query_embedding = model.encode(query).reshape(1, -1)

    scores = []

    for record in vector_store:

        doc_embedding = [record["embedding"]]

        similarity = cosine_similarity(query_embedding, doc_embedding)[0][0]

        scores.append((similarity, record["text"]))

    scores.sort(reverse=True)

    results = [text for _, text in scores[:top_k]]

    return results


def generate_explanation(query, docs):

    context = " ".join(docs)

    explanation = f"""
Topic: {query}

Explanation based on knowledge base:

{context}

Summary:
The above information explains the concept and related ideas.
"""

    return explanation


def recommend_related(query, top_k=2):

    query_embedding = model.encode(query).reshape(1, -1)

    scores = []

    for record in vector_store:

        doc_embedding = [record["embedding"]]

        similarity = cosine_similarity(query_embedding, doc_embedding)[0][0]

        scores.append((similarity, record["text"]))

    scores.sort(reverse=True)

    recs = [text for _, text in scores[:top_k]]

    return recs


def agent_workflow(user_query):

    print("\nStep 1: Searching knowledge base...")

    docs = search_documents(user_query)

    print("Documents retrieved.")

    print("\nStep 2: Generating explanation...")

    explanation = generate_explanation(user_query, docs)

    print("\nStep 3: Finding related topics...")

    recommendations = recommend_related(user_query)

    print("\n===== AI Agent Response =====")

    print(explanation)

    print("\nRecommended Topics:")

    for r in recommendations:
        print("-", r)


if __name__ == "__main__":

    query = input("Enter your topic or question: ")

    agent_workflow(query)