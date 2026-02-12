"""
Updated Logic for keyword gap analysis using the Core Parser.
"""
from core.parser import normalize_text
from typing import List, Tuple, Dict

def ats_analysis(jd_text: str, resume_text: str) -> Tuple[float, Dict[str, int], Dict[str, int]]:
    """
    Standardized entry point for the orchestrator.
    """
    # Use the core parser we refined
    jd_tokens = normalize_text(jd_text)
    resume_tokens = normalize_text(resume_text)

    matched = {}
    missing = {}

    for token, count in jd_tokens.items():
        if token in resume_tokens:
            matched[token] = count
        else:
            missing[token] = count

    # Calculate score
    total_jd_count = len(jd_tokens)
    matched_count = len(matched)
    
    score = 0.0
    if total_jd_count > 0:
        score = round((matched_count / total_jd_count) * 100, 1)

    return score, matched, missing
