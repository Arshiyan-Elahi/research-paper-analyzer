from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/analyze"  # aapka FastAPI backend

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["pdf_file"]
        if file:
            # FastAPI /analyze ko call karo
            files = {"file": (file.filename, file.stream, "application/pdf")}
            resp = requests.post(FASTAPI_URL, files=files)

            if resp.status_code == 200:
                data = resp.json()

                # QA dataset load karo
                qa_samples = []
                try:
                    with open("qa_dataset.jsonl", "r", encoding="utf-8") as f:
                        for line in f:
                            qa_samples.append(json.loads(line))
                except FileNotFoundError:
                    qa_samples = [{"question": "Not generated yet", "answer": ""}]

                return render_template("result.html", metadata=data["metadata"], qa_samples=qa_samples)
            else:
                return f"Error from FastAPI: {resp.text}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
