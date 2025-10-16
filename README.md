# INFOSYS-VIRTUAL-INTERNSHIP-6.0
src/: Python scripts for API calls, preprocessing, and semantic search  notebooks/: Jupyter notebooks for experimentation  data/: YouTube metadata CSV files  models/: Pretrained NLP models or embeddings docs/: Milestone-wise reports and screenshots
# QueryTube: AI Semantic Search for YouTube Data
**Project Statement:**  
QueryTube is a semantic search system that allows users to input natural language queries and retrieve the top-5 most semantically relevant YouTube videos. The project covers metadata extraction, transcript processing, embedding generation, and building a complete semantic search engine.

**Tech Stack:**  
- Python, Pandas/Polars, NumPy  
- YouTube Data API v3, youtube_transcript_api  
- Hugging Face SentenceTransformers  
- Sklearn for distance/similarity metrics  
- Gradio for interactive interface  

## **Project Milestones**

### **Milestone 1: YouTube Data Collection and API Mastery (Weeks 1–2)**
- Extract video metadata (ID, title, date) using YouTube Data API v3  
- Handle pagination and store results in DataFrame  
- EDA on video data (title uniqueness, publish frequency)  
**Deliverables:** Python scripts, cleaned metadata CSV  

### **Milestone 2: Transcript Extraction and Data Cleaning (Weeks 3–4)**
- Extract auto-generated transcripts using `youtube_transcript_api`  
- Clean and normalize transcripts  
- Generate ~70–80 initial search queries  
**Deliverables:** DataFrame with transcript column, cleaning scripts  

### **Milestone 3: Sentence Transformer Evaluation for Semantic Search (Weeks 5–6)**
- Embed titles and transcripts using multiple SentenceTransformer models  
- Evaluate similarity metrics (cosine, euclidean, dot product)  
- Identify best-performing model and metric  
**Deliverables:** Evaluation report, embedding-enriched dataset  

### **Milestone 4: Implementing and Tuning Semantic Search (Weeks 7–8)**
- Implement `returnSearchResults(query, df)` function  
- Optimize thresholds and top_k rankings  
- Build interactive Gradio interface for query-to-top-5 video search  
**Deliverables:** Search function, interactive demo, documentation
  
## **Usage Instructions**

1. Clone the repo:
```bash
git clone https://github.com/<username>/QueryTube-AI-SemanticSearchTube.git
cd QueryTube-AI-SemanticSearchTube
