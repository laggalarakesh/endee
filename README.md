<div style="text-align:center; padding:20px;">

<h1>🤖 AI Knowledge Chatbot</h1>

<p><b>AI-powered document assistant using vector search, RAG, and semantic retrieval built on Endee concepts.</b></p>

<div style="margin:10px;">
  <span style="background:#28a745;color:white;padding:6px 12px;border-radius:6px;margin:5px;">Quick Start</span>
  <span style="background:#007bff;color:white;padding:6px 12px;border-radius:6px;margin:5px;">AI Features</span>
  <span style="background:#fd7e14;color:white;padding:6px 12px;border-radius:6px;margin:5px;">Endee Vector DB</span>
</div>

</div>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project is an <b>AI-powered Knowledge Chatbot</b> that allows users to upload documents (TXT, PDF, DOCX) and interact with them using natural language queries.
</p>

<p>
It demonstrates real-world AI capabilities such as:
</p>

<ul>
<li>Semantic Search</li>
<li>Retrieval Augmented Generation (RAG)</li>
<li>Recommendation Systems</li>
<li>Agentic AI Workflows</li>
</ul>

<hr>

<h2>🎯 Why This Project</h2>

<ul>
<li>Intelligent document understanding</li>
<li>Vector embeddings for semantic retrieval</li>
<li>Real-time chatbot interaction</li>
<li>Modern AI system architecture</li>
</ul>

<hr>

<h2>🚀 Quick Start</h2>

<pre style="background:#f4f4f4;padding:10px;border-radius:8px;">
git clone https://github.com/your-username/endee-ai-assistant.git
cd endee-ai-assistant

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
</pre>

<hr>

<h2>📄 Detailed Project Description</h2>

<p>
This project presents a comprehensive implementation of an AI-powered Knowledge Chatbot designed to interact intelligently with user-provided documents. Users can upload TXT, PDF, or DOCX files and ask natural language questions related to the content.
</p>

<p>
The system leverages advanced AI techniques including vector embeddings, semantic search, Retrieval Augmented Generation (RAG), and recommendation systems. Unlike traditional keyword-based systems, this chatbot understands the meaning of queries and retrieves relevant results even when wording differs.
</p>

<p>
When a document is uploaded, the system extracts text and converts it into embeddings using a Sentence Transformer model. These embeddings are stored in a vector structure inspired by Endee, enabling efficient similarity-based retrieval.
</p>

<p>
When a user asks a question, the system converts the query into an embedding and compares it with stored vectors using cosine similarity. The most relevant content is retrieved and used to generate a structured answer.
</p>

<p>
The chatbot also includes a relevance detection mechanism. If a query is not related to the document, the system clearly informs the user, ensuring accurate and trustworthy responses.
</p>

<p>
Additionally, a recommendation system suggests related topics based on similarity search, helping users explore more relevant content.
</p>

<hr>

<h2>🧠 System Design</h2>

<pre style="background:#f4f4f4;padding:10px;border-radius:8px;">
User Input
   ↓
Embedding Model
   ↓
Vector Database (Endee Concept)
   ↓
Similarity Search
   ↓
Relevant Documents
   ↓
RAG Processing
   ↓
Final Answer + Recommendations
</pre>

<hr>

<h2>⚙️ Tech Stack</h2>

<ul>
<li>Python</li>
<li>Streamlit</li>
<li>Sentence Transformers</li>
<li>Scikit-learn</li>
<li>PyPDF2</li>
<li>python-docx</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre style="background:#f4f4f4;padding:10px;border-radius:8px;">
endee-ai-assistant/
│
├── app.py
├── requirements.txt
├── README.md
└── data/
    └── vector_store.json
</pre>

<hr>

<h2>📊 Example Output</h2>

<pre style="background:#eafaf1;padding:10px;border-radius:8px;">
📚 Answer:
Deepfake is a type of synthetic media created using AI.

🔎 Related Topics:
• Deep learning uses neural networks.
• AI is used in media applications.
</pre>

<hr>

<h2>🚀 Practical Use Cases</h2>

<ul>
<li>Document-based Q&A systems</li>
<li>Educational assistants</li>
<li>Research tools</li>
<li>Enterprise knowledge systems</li>
</ul>

<hr>

<h2>👨‍💻 Developed By</h2>

<p><b>Laggala Rakesh</b></p>
