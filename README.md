# Multi-Source RAG Chatbot

A Retrieval-Augmented Generation (RAG) application built using Python, LangChain, Google Gemini Embeddings, Chroma Vector Database, and Gemini 2.5 Flash.

This project demonstrates how to build a chatbot capable of retrieving information from multiple document sources and generating context-aware responses using Large Language Models (LLMs).

---

## Project Overview

Traditional chatbots rely only on the knowledge available inside the LLM.

RAG (Retrieval-Augmented Generation) improves response quality by retrieving relevant information from external documents before generating answers.

This project supports multiple document formats:

* PDF Documents
* DOCX Documents
* CSV Files

All document content is converted into embeddings and stored inside a Chroma Vector Database for semantic search.

---

## Architecture

```text
PDF
DOCX
CSV
 ↓
Document Loaders
 ↓
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Chroma Vector Database
 ↓
Similarity Search
 ↓
Context Assembly
 ↓
Gemini 2.5 Flash
 ↓
Final Answer
```

---

## Technologies Used

* Python
* LangChain
* LangChain Community
* LangChain Text Splitters
* Google Gemini Embeddings
* Gemini 2.5 Flash
* ChromaDB
* PyPDF
* Docx2txt

---

## Features

### Multi-Source Document Ingestion

Loads and processes:

* PDF documents
* DOCX documents
* CSV files

### Semantic Search

Uses vector embeddings to retrieve relevant information based on meaning rather than exact keywords.

### Vector Database

Stores embeddings in ChromaDB for efficient similarity search.

### Context-Aware Responses

Combines retrieved chunks with user questions before sending them to the LLM.

---

## Project Workflow

### Step 1: Load Documents

```python
PyPDFLoader()
Docx2txtLoader()
CSVLoader()
```

### Step 2: Combine Documents

```python
all_documents = pdf_docs + docx_docs + csv_docs
```

### Step 3: Chunking

```python
RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
```

### Step 4: Embeddings

```python
GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)
```

### Step 5: Vector Database

```python
Chroma.from_documents()
```

### Step 6: Retrieval

```python
vectorstore.similarity_search()
```

### Step 7: Generation

```python
ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)
```

---

## Example Query

Question:

```text
How many paid leave days are employees entitled to?
```

Retrieved Result:

```text
Employees are entitled to 24 paid leave days per year.
```

Generated Answer:

```text
Employees are entitled to 24 paid leave days annually according to the company policy.
```

---

## Project Structure

```text
MULTI_SOURCE_RAG
│
├── multi_source_rag.py
├── company_policy.pdf
├── employee_handbook.docx
├── employee.csv
├── requirements.txt
├── README.md
└── screenshots
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/multi_source_rag.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python multi_source_rag.py
```

---

## Learning Outcomes

Through this project I learned:

* Multi-source document ingestion
* Document chunking strategies
* Embedding generation
* Vector databases
* Semantic search
* Retrieval-Augmented Generation (RAG)
* LangChain integration
* Gemini API integration

---

## Future Enhancements

* Excel File Support
* Website URL Support
* Metadata Filtering
* Source Citations
* FastAPI Integration
* Docker Deployment
* Azure Deployment
* LangGraph Integration

---

## Author

Pankaj Kumar Das

LinkedIn:
https://www.linkedin.com/in/pankajkrdas/

GitHub:
https://github.com/pankajKxyz2018
