from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load vector database
with open("data/vector_store.json", "r", encoding="utf-8") as f:
    vector_store = json.load(f)


def retrieve_documents(query, top_k=3):
    query_embedding = model.encode(query).reshape(1, -1)

    scores = []

    for record in vector_store:
        doc_embedding = [record["embedding"]]

        similarity = cosine_similarity(query_embedding, doc_embedding)[0][0]

        scores.append((similarity, record["text"]))

    scores.sort(reverse=True)

    results = [text for _, text in scores[:top_k]]

    return results


def generate_answer(query, context_docs):

    context = " ".join(context_docs)

    answer = f"""
Question: {query}

Based on the knowledge base:

{context}

Answer:
The information above explains the concept related to your question.
"""

    return answer


if __name__ == "__main__":

    question = input("Ask a question: ")

    docs = retrieve_documents(question)

    answer = generate_answer(question, docs)

    print("\nRetrieved Documents:\n")

    for d in docs:
        print("-", d)

    print("\nGenerated Answer:\n")

    print(answer)