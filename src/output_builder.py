def build_ml_output(candidate_name, job_id, match_score, skill_gap):
    return {
        "candidate_name": candidate_name,
        "job_id": job_id,
        "match_score_percent": match_score,
        "matched_skills": skill_gap["matched_skills"],
        "missing_skills": skill_gap["missing_skills"],
        "recommendations": skill_gap["suggestions"]
    }
