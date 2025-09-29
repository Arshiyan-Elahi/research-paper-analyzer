from fastapi import FastAPI, UploadFile, File
import httpx
from bs4 import BeautifulSoup
import json, re, datetime

app = FastAPI()

CURRENT_YEAR = datetime.datetime.now().year

# ------------------------
# Helper functions
# ------------------------
def _txtjoin(items):
    return " ".join([i.strip() for i in items if i and i.strip()])

def _first(items, default=""):
    return items[0].strip() if items else default

def _normspace(s):
    return re.sub(r"\s+", " ", s or "").strip()

def _extract_year(text_or_attr):
    if not text_or_attr:
        return None
    m = re.search(r"\b(18|19|20)\d{2}\b", text_or_attr)
    return int(m.group(0)) if m else None


# ------------------------
# Parser with BeautifulSoup
# ------------------------
def parse_grobid_soup(xml_content: str):
    soup = BeautifulSoup(xml_content, "xml")

    # --- Metadata ---
    title = soup.find("title", {"type": "main"}).text if soup.find("title", {"type": "main"}) else "No Title Found"

    # Authors + affiliations
    authors_list = []
    for a in soup.find_all("author"):
        name = _txtjoin([t.get_text() for t in a.find_all(["persName","forename","surname"])])
        aff = _txtjoin([t.get_text() for t in a.find_all("affiliation")])
        if name:
            authors_list.append({"name": name, "affiliation": aff})

    # Venue
    venue_tag = soup.find("title", {"level": ["j", "m"]})
    venue = venue_tag.text.strip() if venue_tag else "Unknown"

    # DOI
    doi_tag = soup.find("idno", {"type": "DOI"})
    doi = doi_tag.text.strip() if doi_tag else "Not Available"

    # Year
    year_texts = []
    for d in soup.find_all("date"):
        if d.get("when"):
            year_texts.append(d["when"])
        if d.text:
            year_texts.append(d.text)
    year = _extract_year(_first(year_texts))

    # Keywords
    keywords = [kw.text.strip() for kw in soup.find_all("term") if kw.text.strip()]

    # Sections
    sections = []
    for div in soup.find_all("div"):
        label = div.get("type") or (div.head.get_text() if div.head else "Section")
        text = _normspace(_txtjoin([p.get_text() for p in div.find_all("p")]))
        if text:
            sections.append({"label": label.lower(), "text": text})

    def _find_section(name):
        for s in sections:
            if name in s["label"]:
                return s["text"]
        return ""

    abstract_text = _normspace(soup.find("abstract").get_text(" ", strip=True)) if soup.find("abstract") else _find_section("abstract")
    intro_text = _find_section("introduction")
    concl_text = _find_section("conclusion")

    # References
    references = []
    for i, b in enumerate(soup.find_all("biblStruct"), start=1):
        ref_id = f"ref_{i}"
        r_title = ""
        if b.analytic and b.analytic.title:
            r_title = b.analytic.title.get_text()
        elif b.monogr and b.monogr.title:
            r_title = b.monogr.title.get_text()

        r_auth = []
        for auth in b.find_all("author"):
            fname = auth.forename.get_text() if auth.forename else ""
            lname = auth.surname.get_text() if auth.surname else ""
            full = f"{fname} {lname}".strip()
            if full:
                r_auth.append(full)

        r_year = None
        if b.imprint and b.imprint.date:
            r_year = _extract_year(b.imprint.date.get_text())

        r_doi = b.find("idno", {"type": "DOI"}).get_text() if b.find("idno", {"type": "DOI"}) else ""

        references.append({
            "ref_id": ref_id,
            "title": r_title,
            "authors": r_auth,
            "year": int(r_year) if r_year else None,
            "doi": r_doi
        })

    # Citations
    citations = []
    for r in soup.find_all("ref", {"type": "bibr"}):
        marker = r.get_text(strip=True)
        sec_div = r.find_parent("div")
        sec_label = sec_div.get("type") if sec_div and sec_div.get("type") else (sec_div.head.get_text() if sec_div and sec_div.head else "")
        targets = r.get("target").split() if r.get("target") else []
        for t in targets:
            ref_id = t.lstrip("#")
            citations.append({
                "ref_xml_id": ref_id,
                "marker": marker.strip("[],"),
                "section": sec_label.lower() if sec_label else ""
            })

    return {
        "metadata": {
            "title": title,
            "authors": authors_list,
            "venue": venue,
            "year": int(year) if year else None,
            "doi": doi,
            "keywords": keywords
        },
        "sections": {
            "abstract": abstract_text,
            "introduction": intro_text,
            "conclusion": concl_text,
            "all": sections
        },
        "references": references,
        "citations": citations
    }


# ------------------------
# Cleanup Step
# ------------------------
def cleanup_metadata(data: dict) -> dict:
    seen, clean_authors = set(), []
    for a in data["metadata"]["authors"]:
        name = a.get("name", "").strip()
        if name and name not in seen:
            seen.add(name)
            clean_authors.append(a)
    data["metadata"]["authors"] = clean_authors
    return data


# ------------------------
# FastAPI endpoint
# ------------------------
@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    files = {"input": (file.filename, await file.read(), "application/pdf")}
    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(
            "http://localhost:8070/api/processFulltextDocument",
            files=files
        )

    if resp.status_code != 200:
        return {"error": f"GROBID failed with status {resp.status_code}"}

    xml_content = resp.text
    data = parse_grobid_soup(xml_content)
    data = cleanup_metadata(data)

    # ✅ Export sections.jsonl
    with open("sections.jsonl", "w", encoding="utf-8") as f:
        for s in data["sections"]["all"]:
            json.dump({"section": s["label"], "text": s["text"]}, f, ensure_ascii=False)
            f.write("\n")

    # ✅ Export qa_dataset.jsonl
    with open("qa_dataset.jsonl", "w", encoding="utf-8") as f:
        for s in data["sections"]["all"]:
            context = s["text"]
            label = s["label"]

            if "abstract" in label:
                q, a = "What is the paper about?", context
            elif "introduction" in label:
                q, a = "What problem does the paper address?", context
            elif "conclusion" in label:
                q, a = "What are the main findings of the paper?", context
            else:
                q, a = f"What is discussed in the {label} section?", context

            if len(a) > 700:
                a = a[:500] + "..."

            json.dump({"context": context, "question": q, "answer": a}, f, ensure_ascii=False)
            f.write("\n")

    return data
