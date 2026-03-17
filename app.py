import streamlit as st
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os
from PyPDF2 import PdfReader
from docx import Document

# ===============================
# ⚙️ CONFIG
# ===============================
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

model = SentenceTransformer('all-MiniLM-L6-v2')
VECTOR_FILE = "data/vector_store.json"

# ===============================
# 📦 VECTOR DB FUNCTIONS
# ===============================
def load_vectors():
    if os.path.exists(VECTOR_FILE):
        with open(VECTOR_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_vectors(data):
    with open(VECTOR_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# ===============================
# 📄 FILE EXTRACTION
# ===============================
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# ===============================
# 🧠 STORE DOCUMENT (FIXED)
# ===============================
def store_uploaded_doc(text, replace=True):
    if replace:
        data = []  # clear old DB
    else:
        data = load_vectors()

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines:
        embedding = model.encode(line).tolist()
        data.append({"text": line, "embedding": embedding})

    save_vectors(data)

# ===============================
# 🔍 SEARCH (FIXED)
# ===============================
def search_with_scores(query, top_k=3):
    data = load_vectors()  # always reload

    if len(data) == 0:
        return []

    query_embedding = model.encode(query).reshape(1, -1)

    scores = []

    for record in data:
        doc_embedding = [record["embedding"]]
        sim = cosine_similarity(query_embedding, doc_embedding)[0][0]
        scores.append((sim, record["text"]))

    scores.sort(reverse=True)

    return scores[:top_k]

# ===============================
# 🎯 RELEVANCE CHECK (FIXED)
# ===============================
def is_relevant(results, threshold=0.3):  # lowered threshold
    if not results:
        return False
    return results[0][0] > threshold

# ===============================
# 🧠 AGENT LOGIC
# ===============================
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

# ===============================
# 🎨 UI & NAVIGATION
# ===============================
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Feature",
    ["Chatbot", "Ingest Data", "Semantic Search", "Recommendations", "Agent Workflow"]
)

if page == "Chatbot":
    st.title("🤖 AI Knowledge Chatbot")
    st.markdown("Upload document + Ask questions in one place")

    # Chat memory
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # ===============================
    # 📤 Upload Document
    # ===============================
    uploaded_file = st.file_uploader(
        "Upload TXT / PDF / DOCX",
        type=["txt", "pdf", "docx"]
    )

    if uploaded_file:
        file_type = uploaded_file.name.split(".")[-1]

        if file_type == "txt":
            content = uploaded_file.read().decode("utf-8")

        elif file_type == "pdf":
            content = extract_text_from_pdf(uploaded_file)

        elif file_type == "docx":
            content = extract_text_from_docx(uploaded_file)

        else:
            content = ""

        st.subheader("Preview")
        st.text(content[:500])

        if st.button("📥 Store Document"):
            store_uploaded_doc(content, replace=True)
            st.success("✅ Document stored (old data cleared)")

    # ===============================
    # 💬 Chat Input
    # ===============================
    user_input = st.chat_input("Ask about your document...")

    if user_input:

        st.session_state.chat_history.append(("user", user_input))

        results = search_with_scores(user_input)

        # ❌ Not relevant
        if not is_relevant(results):
            bot_reply = "❌ This question is not related to your document."

        # ✅ Relevant
        else:
            context = "\n".join([text for _, text in results])

            answer = f"📚 Answer:\n{context}"

            recs = [text for _, text in results[:2]]

            bot_reply = answer + "\n\n🔎 Related Topics:\n"
            for r in recs:
                bot_reply += f"- {r}\n"

        st.session_state.chat_history.append(("bot", bot_reply))

    # ===============================
    # 💬 Display Chat
    # ===============================
    for role, message in st.session_state.chat_history:
        if role == "user":
            with st.chat_message("user"):
                st.write(message)
        else:
            with st.chat_message("assistant"):
                st.write(message)

elif page == "Ingest Data":
    st.title("📥 Ingest Data")
    st.markdown("Load knowledge base directly from `data/knowledge_base.txt`.")
    if st.button("Start Ingestion"):
        kb_path = "data/knowledge_base.txt"
        if os.path.exists(kb_path):
            with open(kb_path, "r", encoding="utf-8") as f:
                documents = f.readlines()
            
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
                
            save_vectors(vector_store)
            st.success("✅ Data successfully converted into embeddings and stored.")
        else:
            st.error("❌ Knowledge base file not found!")

elif page == "Semantic Search":
    st.title("🔍 Semantic Search")
    query = st.text_input("Enter your search query:")
    if query:
        results = search_with_scores(query, top_k=3)
        st.subheader("Top Results:\n")
        for score, text in results:
            st.markdown(f"**{score:.3f}** → {text}")

elif page == "Recommendations":
    st.title("💡 Recommendations")
    topic = st.text_input("Enter a topic to get recommendations:")
    if topic:
        results = search_with_scores(topic, top_k=3)
        st.subheader("Recommended Topics:\n")
        for _, text in results:
            st.markdown(f"- {text}")

elif page == "Agent Workflow":
    st.title("🤖 Agent Workflow")
    query = st.text_input("Enter your topic or question:")
    if query:
        st.markdown("### Step 1: Searching knowledge base...")
        results = search_with_scores(query, top_k=3)
        docs = [text for _, text in results]
        st.success("Documents retrieved.")
        
        st.markdown("### Step 2: Generating explanation...")
        explanation = generate_explanation(query, docs)
        
        st.markdown("### Step 3: Finding related topics...")
        recommendations = [text for _, text in results[:2]]
        
        st.markdown("---")
        st.markdown("## ===== AI Agent Response =====")
        st.text(explanation)
        
        st.markdown("**Recommended Topics:**")
        for r in recommendations:
            st.markdown(f"- {r}")