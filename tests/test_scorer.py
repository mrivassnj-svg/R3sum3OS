import pytest
from core.scorer import score_skill

def test_weight_hierarchy():
    """Verify core_skills (3.0) score higher than soft_skills (1.0)."""
    core_score = score_skill("core_skill", 1.0)
    soft_score = score_skill("soft_skill", 1.0)
    
    assert core_score == 3.0
    assert soft_score == 1.0
    assert core_score > soft_score

def test_unknown_category_fallback():
    """Ensure the scorer doesn't crash on an unknown category."""
    # Should fallback to 'other' weight (0.5)
    score = score_skill("mystery_category", 1.0)
    assert score == 0.5
