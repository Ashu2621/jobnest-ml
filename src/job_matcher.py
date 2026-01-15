from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# STEP 2: Match Score Calculator
def calculate_match_score(resume_text, job_text):
    corpus = [resume_text, job_text]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = round(similarity[0][0] * 100, 2)

    return score


# STEP 3: Missing Skills Finder
def find_missing_skills(resume_text, job_text):
    resume_words = set(resume_text.split())
    job_words = set(job_text.split())

    missing = job_words - resume_words
    return list(missing)
