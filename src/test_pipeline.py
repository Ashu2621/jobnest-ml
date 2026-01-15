from resume_parser import extract_text_from_pdf
from text_cleaner import clean_text
from job_parser import load_job_description
from job_matcher import calculate_match_score
from skill_gap_analyzer import analyze_skill_gap
from output_builder import build_ml_output

# Load resume
resume = extract_text_from_pdf("../data/resumes/sample.pdf")
clean_resume = clean_text(resume)

# Load job
job_id = "job1"
job = load_job_description("../data/jobs/job1.txt")
clean_job = clean_text(job)

# ML processing
score = calculate_match_score(clean_resume, clean_job)
skill_gap = analyze_skill_gap(clean_resume, clean_job)

final_output = build_ml_output(
    candidate_name="Ashutosh Sharma",
    job_id=job_id,
    match_score=score,
    skill_gap=skill_gap
)

print(final_output)
