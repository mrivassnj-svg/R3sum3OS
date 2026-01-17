from collections import Counter
from core.scorer import calculate_weighted_ats_score


def test_weighted_score():
    resume = Counter({"python": 2, "sql": 1})
    jd = Counter({"python": 1, "sql": 1, "docker": 1})

    ontology = {
        "python": "core_skill",
        "sql": "core_skill",
        "docker": "tool"
    }

    score = calculate_weighted_ats_score(resume, jd, ontology)
    assert 0 <= score <= 100
