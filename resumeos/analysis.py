"""
Logic for keyword gap analysis and ATS matching.
"""
from collections import Counter
from typing import List, Tuple

def perform_gap_analysis(resume_tokens: Counter, jd_tokens: Counter) -> Tuple[List[str], List[str]]:
    """
    Identifies matched keywords and missing gaps between resume and JD.
    
    Returns:
        Tuple containing (list of matched tokens, list of missing tokens)
    """
    matched = []
    missing = []

    # Iterate through tokens required by the Job Description
    for token in jd_tokens:
        if token in resume_tokens:
            matched.append(token)
        else:
            missing.append(token)
            
    # Return sorted lists for consistent UI display
    return sorted(matched), sorted(missing)

def calculate_match_percentage(matched_count: int, total_jd_count: int) -> float:
    """
    Calculates the raw match percentage.
    """
    if total_jd_count == 0:
        return 0.0
    return round((matched_count / total_jd_count) * 100, 1)
