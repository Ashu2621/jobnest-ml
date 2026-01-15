from job_matcher import calculate_match_score


def recommend_jobs(clean_resume, jobs_dict, top_n=3):
    """
    clean_resume: cleaned resume text
    jobs_dict: {job_id: cleaned_job_text}
    top_n: number of jobs to recommend
    """

    scores = []

    for job_id, job_text in jobs_dict.items():
        score = calculate_match_score(clean_resume, job_text)
        scores.append((job_id, score))

    # Sort by score descending
    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top_n]
