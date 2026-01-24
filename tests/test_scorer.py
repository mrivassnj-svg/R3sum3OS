import pytest
from collections import Counter
from core.scorer import calculate_weighted_ats_score

def test_perfect_match():
    """If the resume contains everything in the JD, the score should be 100%."""
    resume = Counter(["python", "sql", "docker"])
    jd = Counter(["python", "sql", "docker"])
    ontology = {"python": "technical_skill", "sql": "technical_skill", "docker": "tool"}
    
    score = calculate_weighted_ats_score(resume, jd, ontology)
    assert score == 100

def test_zero_match():
    """If there is no overlap, the score should be 0%."""
    resume = Counter(["cooking", "painting"])
    jd = Counter(["python", "sql"])
    ontology = {"python": "technical_skill", "sql": "technical_skill"}
    
    score = calculate_weighted_ats_score(resume, jd, ontology)
    assert score == 0

def test_partial_match_weighting():
    """Verify that different categories impact the score differently."""
    # weights: technical=1.0, other=0.1
    ontology = {"python": "technical_skill", "teamwork": "other"}
    
    jd = Counter(["python", "teamwork"])
    # Case 1: Match the high-weight skill
    resume_high = Counter(["python"])
    score_high = calculate_weighted_ats_score(resume_high, jd, ontology)
    
    # Case 2: Match the low-weight skill
    resume_low = Counter(["teamwork"])
    score_low = calculate_weighted_ats_score(resume_low, jd, ontology)
    
    assert score_high > score_low
