from core.ontology import load_ontology
from core.scorer import calculate_weighted_ats_score
from core.parser import normalize_text

def analyze_resume(resume: str, job_desc: str, role: str = "software_engineer") -> str:
    resume_tokens = normalize_text(resume)
    jd_tokens = normalize_text(job_desc)

    ontology = load_ontology(role)

    score = calculate_weighted_ats_score(
        resume_tokens,
        jd_tokens,
        ontology
    )

    return f"""
╔══════════════════════════════════════╗
║ ATS WEIGHTED SCORE :: {score}%        
╚══════════════════════════════════════╝
"""
