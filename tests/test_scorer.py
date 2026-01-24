import pytest
from collections import Counter
from core.scorer import calculate_weighted_ats_score

# Mock weights for testing purposes
MOCK_ONTOLOGY = {
    "python": "technical_skill",
    "sql": "technical_skill",
    "docker": "tool",
    "communication": "soft_skill"
}

def test_perfect_match_score():
    """Verify that a perfect overlap results in a 100% score."""
    resume = Counter(["python", "sql", "docker"])
    jd = Counter(["python", "sql", "docker"])
    
    score = calculate_weighted_ats_score(resume, jd, MOCK_ONTOLOGY)
    assert score == 100

def test_partial_match_weighting():
    """Verify that technical skills carry more weight than tools or others."""
    jd = Counter(["python", "docker"])
    
    # Match ONLY the technical skill (Weight 1.0)
    high_weight_resume = Counter(["python"])
    high_score = calculate_weighted_ats_score(high_weight_resume, jd, MOCK_ONTOLOGY)
    
    # Match ONLY the tool (Weight 0.7)
    low_weight_resume = Counter(["docker"])
    low_score = calculate_weighted_ats_score(low_weight_resume, jd, MOCK_ONTOLOGY)
    
    assert high_score > low_score

def test_frequency_capping():
    """Ensure that repeating a keyword in the resume doesn't 'cheat' the score."""
    jd = Counter(["python"]) # JD only asks for it once
    resume = Counter(["python", "python", "python"]) # Candidate says it thrice
    
    score = calculate_weighted_ats_score(resume, jd, MOCK_ONTOLOGY)
    assert score == 100 # Should not exceed 100% based on over-repetition

def test_zero_match_score():
    """Verify that no overlap results in a 0% score."""
    resume = Counter(["cooking", "gardening"])
    jd = Counter(["python", "sql"])
    
    score = calculate_weighted_ats_score(resume, jd, MOCK_ONTOLOGY)
    assert score == 0
