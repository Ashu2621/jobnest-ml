from flask import Flask, request, jsonify
import pdfplumber
import os
import tempfile

from src.text_cleaner import clean_text
from src.job_matcher import calculate_match_score
from src.skill_gap_analyzer import analyze_skill_gap

app = Flask(__name__)

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


@app.route("/match-file", methods=["POST"])
def match_file():
    if "resume" not in request.files:
        return {"error": "Resume file missing"}, 400

    resume_file = request.files["resume"]
    job_text = request.form.get("job_text", "")

    if not job_text:
        return {"error": "job_text missing"}, 400

    resume_text = extract_text_from_pdf(resume_file)

    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_text)

    score = calculate_match_score(clean_resume, clean_job)
    skill_gap = analyze_skill_gap(clean_resume, clean_job)

    return jsonify({
        "match_score_percent": float(score),
        "matched_skills": skill_gap["matched_skills"],
        "missing_skills": skill_gap["missing_skills"],
        "recommendations": skill_gap["suggestions"]
    }), 200


@app.route("/health")
def health():
    return {"status": "ML API running"}
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
