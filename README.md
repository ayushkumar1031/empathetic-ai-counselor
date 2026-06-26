# Empathetic AI Counselor

> 🚧 **Project Status:** Under Active Development

An AI-powered counseling assistant that understands a user's emotional state, maintains conversation memory, retrieves relevant mental health knowledge using Retrieval-Augmented Generation (RAG), and generates context-aware empathetic responses using a Large Language Model (LLM).

The goal of this project is to build an intelligent conversational system that responds with empathy by combining emotion detection, conversation history, emotional trajectory analysis, and knowledge retrieval instead of relying solely on an LLM.

---

## Features

* Emotion classification using Hugging Face Transformers
* Emotion analysis with intensity and concern detection
* Conversation memory for maintaining dialogue history
* Emotional trajectory tracking across conversations
* Retrieval-Augmented Generation (RAG) using ChromaDB
* Semantic search using Sentence Transformers
* Context-aware prompt construction
* Empathetic response generation using Groq LLM
* Unit tests for core components

---

## Architecture

```text
User Message
      │
      ▼
Emotion Classification
      │
      ▼
Emotion Analysis
      │
      ▼
Conversation Memory
      │
      ▼
Emotional Trajectory Tracking
      │
      ▼
Knowledge Retrieval (RAG)
      │
      ▼
Context Builder
      │
      ▼
Groq LLM
      │
      ▼
Empathetic Response
```

---

## Tech Stack

**Languages**

* Python

**AI / Machine Learning**

* Hugging Face Transformers
* Sentence Transformers
* Groq API

**Vector Database**

* ChromaDB

**Backend**

* FastAPI

**Testing**

* Pytest

**Version Control**

* Git
* GitHub

---

## Project Structure

```text
empathetic-ai-counselor/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── prompts/
│   │   └── services/
│   ├── tests/
│   └── demo1.py
│
├── data/
│   ├── processed/
│   └── ingest.py
│
└── README.md
```

---

## Implemented Modules

* Emotion Classification
* Emotion Analysis
* Conversation Memory
* Emotional Trajectory Tracking
* Retrieval-Augmented Generation (RAG)
* Context Builder
* Groq LLM Integration

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/ayushkumar1031/empathetic-ai-counselor.git
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Create a `.env` file inside the `backend` directory and add your Groq API key:

```text
GROQ_API_KEY=your_api_key
```

Run the demo:

```bash
python backend/demo1.py
```

Run tests:

```bash
pytest
```

---

## Current Progress

✔ Phase 0 – Project Setup

✔ Phase 1 – Emotion Classification

✔ Phase 2 – Emotion Analysis

✔ Phase 3 – Empathetic Response Generation

✔ Phase 4 – Conversation Memory

✔ Phase 5 – Emotional Trajectory Tracking

✔ Phase 6 – RAG Knowledge Base

✔ Phase 7 – Retrieval Integration

---

## Future Work

* Backend API integration
* Frontend integration
* Persistent conversation storage
* Advanced retrieval strategies
* Response evaluation
* Deployment
* Additional safety mechanisms

---

## Note

This project is currently under active development. Additional features, optimizations, and deployment support will be added in future phases.
