
````markdown
# 📑 Research Paper Analysis & Q/A Generator

This project automates the **extraction and analysis of research papers**.  
It integrates **[GROBID](https://github.com/kermitt2/grobid)** for structured data extraction, a **FastAPI backend** for parsing XML into JSON, and a **Flask frontend** for displaying metadata and generating **Q/A pairs**.

---

## 🚀 Features
- 📄 Extracts **Title, Authors, Affiliations, Venue, Year, DOI, Keywords**
- 📝 Splits paper into **sections** (Abstract, Introduction, Conclusion, etc.)
- 🔗 Extracts **References & Citations**
- ❓ Auto-generates **Q/A dataset** from sections (`qa_dataset.jsonl`)
- 🌐 Provides **Flask-based UI** to upload PDFs and view results
- ⚡ Modular: FastAPI for backend + Flask for frontend

---

## 🏗 System Architecture

```mermaid
graph TD;
    PDF["Research Paper PDF"] --> GROBID["📦 GROBID (Docker)"];
    GROBID --> XML["TEI XML"];
    XML --> FastAPI["⚡ FastAPI Backend"];
    FastAPI --> JSON["Q/A Dataset (JSONL)"];
    JSON --> Flask["🌐 Flask Frontend"];
    Flask --> User["👤 User Interface"];
````

---

## 🛠 Tech Stack

* **Python 3.10+**
* **FastAPI** (Backend API)
* **Flask** (Frontend UI)
* **Docker** (Run GROBID 0.7.3)
* **BeautifulSoup4 / lxml** (XML parsing)
* **httpx / requests** (API communication)
* **Bootstrap 5** (Frontend styling)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/research-paper-analyzer.git
cd research-paper-analyzer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run GROBID (Docker)

```bash
docker run -t --rm -p 8070:8070 grobid/grobid:0.7.3
```

Check service:

```bash
curl http://localhost:8070/api/isalive
```

---

## ▶️ How to Run the Application (Step by Step)

**Step 1:** Start **FastAPI Backend**

```bash
cd fastapi_backend
uvicorn test:app --reload --port 8000
```

* Open Swagger Docs here: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

**Step 2:** Start **Flask Frontend**

```bash
cd flask_app
python app.py
```

* Open the app here: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

**Step 3:** Upload PDF in Flask UI

* Select any research paper PDF
* Click **Analyze**
* You will see:

  * Extracted **Metadata** (Title, Authors, Year, DOI, Venue, etc.)
  * Auto-generated **Q/A pairs** from paper sections

---

## 📂 Project Structure

```
ResearchPaperQA/
│── README.md
│── requirements.txt
│── fastapi_backend/
│    └── test.py         # FastAPI XML → JSON parser
│── flask_app/
│    ├── app.py          # Flask frontend
│    └── templates/
│         ├── index.html
│         └── result.html
│── sample_files/
│    ├── sample.pdf
│    └── qa_dataset.jsonl
│── docker-compose.yml   # Optional
```

---

## 📊 Example Q/A Output (qa_dataset.jsonl)

```json
{
  "question": "What problem does the paper address?",
  "answer": "This paper introduces deep residual networks to improve image recognition accuracy...",
  "context": "This paper introduces deep residual networks..."
}
```

---

## 🌟 Future Work

* Use **semantic search** (Sentence-BERT / OpenAI embeddings) for dynamic Q/A
* Add **vector database (FAISS, Pinecone, Qdrant)** for scalable queries
* Improve **UI/UX** with better visualization

---
