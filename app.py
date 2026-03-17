import streamlit as st
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖",
    layout="wide"
)

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load vector store
with open("data/vector_store.json", "r", encoding="utf-8") as f:
    vector_store = json.load(f)


# Semantic search function
def semantic_search(query, top_k=3):
    query_embedding = model.encode(query).reshape(1, -1)

    scores = []

    for record in vector_store:
        doc_embedding = [record["embedding"]]
        similarity = cosine_similarity(query_embedding, doc_embedding)[0][0]

        scores.append((similarity, record["text"]))

    scores.sort(reverse=True)

    return [text for _, text in scores[:top_k]]


# Header
st.title("🤖 AI Knowledge Assistant")
st.markdown("Powered by **Endee Vector Database**")

st.markdown("---")

# Sidebar menu
menu = st.sidebar.radio(
    "Choose Feature",
    [
        "🏠 Home",
        "🔍 Semantic Search",
        "❓ Ask Question (RAG)",
        "⭐ Recommendations",
        "🧠 AI Agent Workflow"
    ]
)

# Home Page
if menu == "🏠 Home":

    st.header("Welcome to AI Knowledge Assistant")

    st.write(
        """
This application demonstrates how **vector databases and embeddings** 
can power intelligent AI systems.

Features included:
- Semantic Search
- Retrieval Augmented Generation (RAG)
- Recommendation System
- Agentic AI Workflow
"""
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("🔍 Semantic Search\n\nFind documents using meaning instead of keywords.")

        st.info("❓ RAG Question Answering\n\nAsk questions and retrieve answers from knowledge base.")

    with col2:
        st.info("⭐ Recommendation Engine\n\nGet related topic suggestions.")

        st.info("🧠 AI Agent\n\nAutomated workflow combining search, reasoning and suggestions.")


# Semantic Search
elif menu == "🔍 Semantic Search":

    st.header("🔍 Semantic Search")

    query = st.text_input("Enter search query")

    if st.button("Search"):

        results = semantic_search(query)

        st.subheader("Results")

        for r in results:
            st.success(r)


# RAG Question Answering
elif menu == "❓ Ask Question (RAG)":

    st.header("❓ Ask a Question")

    question = st.text_input("Enter your question")

    if st.button("Generate Answer"):

        docs = semantic_search(question)

        st.subheader("Retrieved Knowledge")

        for d in docs:
            st.write("•", d)

        context = " ".join(docs)

        st.subheader("Generated Answer")

        st.info(context)


# Recommendation System
elif menu == "⭐ Recommendations":

    st.header("⭐ Topic Recommendations")

    topic = st.text_input("Enter a topic")

    if st.button("Get Recommendations"):

        recs = semantic_search(topic)

        st.subheader("Recommended Topics")

        for r in recs:
            st.success(r)


# AI Agent Workflow
elif menu == "🧠 AI Agent Workflow":

    st.header("🧠 AI Research Agent")

    query = st.text_input("Enter topic or question")

    if st.button("Run AI Agent"):

        st.subheader("Step 1 — Searching Knowledge Base")

        docs = semantic_search(query)

        for d in docs:
            st.write("•", d)

        st.subheader("Step 2 — Explanation")

        context = " ".join(docs)

        st.info(context)

        st.subheader("Step 3 — Recommended Topics")

        recs = semantic_search(query)

        for r in recs[:2]:
            st.success(r)