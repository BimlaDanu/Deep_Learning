faq-vector-search/
|--   app.py
|---  data.py
|---  requirements.txt
|---  README.md

```bash
pip install -r requirements.txt
```

- Build a small system where users ask questions and get relevant answers using a vector database.

    - User -> API -> Embedding -> Vector DB -> Top match -> Answer

**FastAPI:** A modern Python framework for building fast APIs with automatic validation and documentation.

**Uvicorn:** A lightweight, high-performance server used to run FastAPI applications.

**FAISS:**  A library for efficient similarity search over high-dimensional vectors (used as a vector database).

**sentence-transformers:** A library that converts text into semantic vector embeddings using transformer models.

**Streamlit:** A tool for quickly building interactive web apps and dashboards for machine learning projects.