import re
from collections import Counter

STOPWORDS = {
    "and","or","the","with","to","of","in","for","a","an","on",
    "using","used","work","worked","team","teams","project","projects","helped"
}

def normalize(text: str):
    if not text:
        return []
    return [
        w.lower()
        for w in re.findall(r"[a-zA-Z]{3,}", text)
        if w.lower() not in STOPWORDS
    ]

def ats_analysis(job_desc: str, profile_text: str):
    job_terms = normalize(job_desc)
    profile_terms = normalize(profile_text)

    job_counts = Counter(job_terms)
    profile_set = set(profile_terms)

    matched = {k: v for k, v in job_counts.items() if k in profile_set}
    missing = {k: v for k, v in job_counts.items() if k not in profile_set}

    score = round(
        (sum(matched.values()) / sum(job_counts.values())) * 100, 1
    ) if job_counts else 0.0

    return score, matched, missing
