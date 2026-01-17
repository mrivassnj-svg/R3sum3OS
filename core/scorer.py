"""
Weighted ATS scoring engine.
"""

from collections import Counter
from typing import Dict, Set

from core.weights import DEFAULT_WEIGHTS


def calculate_weighted_ats_score(
    resume_tokens: Counter,
    jd_tokens: Counter,
    ontology: Dict[str, str]
) -> int:
    """
    Calculates weighted ATS score based on ontology categories.
    """

    if not jd_tokens:
        return 0

    score = 0.0
    max_score = 0.0

    for token, jd_freq in jd_tokens.items():
        category = ontology.get(token, "other")
        weight = DEFAULT_WEIGHTS.get(category, DEFAULT_WEIGHTS["other"])

        max_score += weight * jd_freq

        if token in resume_tokens:
            score += weight * min(resume_tokens[token], jd_freq)

    return int((score / max_score) * 100) if max_score else 0
