SKILLS = {
    "java", "python", "spring", "springboot",
    "react", "node", "nodejs", "mongodb",
    "express", "javascript", "mysql",
    "redis", "git", "rest", "apis"
}

def analyze_skill_gap(clean_resume, clean_job):
    resume_words = set(clean_resume.split()) & SKILLS
    job_words = set(clean_job.split()) & SKILLS

    matched_skills = sorted(resume_words & job_words)
    missing_skills = sorted(job_words - resume_words)

    suggestions = [
        f"Consider learning or adding experience in {skill}"
        for skill in missing_skills
    ]

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }
