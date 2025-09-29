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
