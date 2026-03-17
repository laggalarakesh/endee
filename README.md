Project Roadmap
Offline AI Knowledge Assistant using Endee

Goal: Build one project that demonstrates

Semantic Search

RAG (Retrieval Augmented Generation)

Recommendation System

Agentic AI Workflow

🗺 Phase 1 — Repository Setup (30–40 minutes)
Step 1

Open the official repository.

Star it and fork it.

Step 2

Clone your forked repository locally.

Example:

git clone https://github.com/your-username/endee
cd endee
Step 3

Create a project folder inside the repo.

Example:

endee-ai-project

Folder structure:

endee-ai-project
│
├── app.py
├── ingest_data.py
├── semantic_search.py
├── rag_pipeline.py
├── recommendation.py
├── agent_workflow.py
├── requirements.txt
├── README.md
└── data
     └── knowledge_base.txt
🗺 Phase 2 — Environment Setup (20 minutes)

Install dependencies.

Example requirements:

sentence-transformers
transformers
torch
streamlit
numpy
pandas

Install:

pip install -r requirements.txt
🗺 Phase 3 — Prepare Knowledge Dataset (30 minutes)

Create a dataset file.

Example:

data/knowledge_base.txt

Example content:

Artificial Intelligence is the simulation of human intelligence by machines.

Machine learning is a subset of AI that learns from data.

Deep learning uses neural networks with multiple layers.

Vector databases store embeddings for semantic search.

This will be stored in the vector database.

🗺 Phase 4 — Data Ingestion (1 hour)

Goal: Convert text → embeddings → store in Endee.

Steps:

Load documents

Generate embeddings

Store embeddings in Endee vector DB

Flow:

Documents
   ↓
Embedding Model
   ↓
Vector Representation
   ↓
Store in Endee Database

Output:

Vector database containing all knowledge documents.

🗺 Phase 5 — Semantic Search (1 hour)

Goal: Search documents using meaning.

User enters query:

"What is machine learning?"

Process:

Query
 ↓
Embedding
 ↓
Vector Search
 ↓
Top Similar Documents

Return the most relevant documents.

🗺 Phase 6 — RAG Question Answering (1.5 hours)

Goal: Generate answers using retrieved documents.

Pipeline:

User Question
      ↓
Embedding
      ↓
Endee Search
      ↓
Relevant Documents
      ↓
Local Language Model
      ↓
Generated Answer

Example:

Question:

Explain neural networks

System retrieves documents and generates answer.

🗺 Phase 7 — Recommendation System (45 minutes)

Goal: Suggest similar topics.

Example:

User reads:

Deep Learning

System recommends:

Neural Networks
Machine Learning
Artificial Intelligence

Method:

Vector similarity.

🗺 Phase 8 — Agentic AI Workflow (1 hour)

Goal: AI performs multiple tasks automatically.

Example request:

Explain deep learning and suggest resources

Agent performs:

Search database

Retrieve documents

Summarize information

Recommend related topics

Workflow:

User Request
   ↓
Search Knowledge Base
   ↓
Retrieve Documents
   ↓
Generate Summary
   ↓
Suggest Related Topics
🗺 Phase 9 — Build User Interface (1 hour)

Use Streamlit.

Interface layout:

AI Knowledge Assistant
--------------------------

1. Ask Question (RAG)
2. Semantic Search
3. Get Recommendations
4. AI Research Assistant

Example UI elements:

Text input
Search button
Answer display
Recommendation section
🗺 Phase 10 — Testing (45 minutes)

Test all features.

Check:

✔ Data ingestion
✔ Semantic search results
✔ RAG answers
✔ Recommendations
✔ Agent workflow

🗺 Phase 11 — GitHub Documentation (1 hour)

Create a good README.

Include:

Project Overview

Explain the problem and solution.

Features

Semantic Search

RAG

Recommendation

AI Workflow

Architecture Diagram
User
 ↓
Streamlit UI
 ↓
Python Backend
 ↓
Embedding Model
 ↓
Endee Vector Database
 ↓
Local AI Model
Setup Instructions
git clone repo
pip install requirements
streamlit run app.py
Screenshots

Add UI screenshots.

🗺 Phase 12 — Final Submission

Push project to GitHub.

Example:

git add .
git commit -m "AI Knowledge Assistant using Endee"
git push

Then submit the GitHub link in the Google Form