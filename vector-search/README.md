- SCHEMATIC

faq-vector-search/
│
├── app.py
├── data.py
├── requirements.txt
└── README.md


```bash
pip install -r requirements.txt # Setting up the environment
```

```bash
uvicorn app:app --reload # running the app.py
Ctrl + C # stopping the app.py
```

- Build a small system where users ask questions and get relevant answers using a vector database.

- User -> API -> Embedding -> Vector DB -> Top match -> Answer

**FastAPI:** A modern Python framework for building fast APIs with automatic validation and documentation.

**Uvicorn:** A lightweight, high-performance server used to run FastAPI applications.

**FAISS:**  A library for efficient similarity search over high-dimensional vectors (used as a vector database).

**sentence-transformers:** A library that converts text into semantic vector embeddings using transformer models.

**Streamlit:** A tool for quickly building interactive web apps and dashboards for machine learning projects.

Querries on web 
    - http://127.0.0.1:8000/docs
    - http://127.0.0.1:8000/search?query=refund
    - http://127.0.0.1:8000/search?query=change email
    - http://127.0.0.1:8000/docs
    - http://127.0.0.1:8000/search?query=I forgot my password