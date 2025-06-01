# 📚 LangChain Chroma Vector Store + Gemini QA CLI

This project allows you to index markdown files into a [ChromaDB](https://docs.trychroma.com/) vector store using [LangChain](https://python.langchain.com/) and query them interactively via a terminal command, powered by [Google Gemini](https://ai.google.dev/).

---

## ✨ Features

- 📄 Upload markdown (`.md`) files from a directory to ChromaDB with chunking
- 🤖 Query your documents via natural language questions using Google Gemini (gemini-2.0-flash)
- 📚 Source-aware answers with relevance-based retrieval
- ✅ Customizable chunk size, overlap, and persist directory
- 🔒 API key management via `.env` file

---

## 📦 Project Structure

```bash
.
├── resources/                # Markdown files you want to upload
├── chroma/                   # Persisted Chroma vector store directory
├── upload_documents.py       # Script to upload documents to vector store
├── query_chroma.py           # Script to query documents via Gemini
├── .env                      # Your API key config file
├── requirements.txt
└── README.md
```

---

## Running the Code

1. Install the dependencies.
```bash
pip install -r requirements.txt
```

2. Upload the code to ChromaDB.
```bash
python ./upload.py ./your_file_path
```

3. Start the query.
```bash
python ./search.py
```

---

## That was fun! Cheers!!
