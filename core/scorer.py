"""
Defines and applies weighting rules for resume scoring.
"""

from typing import Dict

DEFAULT_WEIGHTS: Dict[str, float] = {
    "technical_skill": 1.0,
    "soft_skill": 0.5,
    "tool": 0.7,
    "certification": 1.2,
    "other": 0.1
}

VALID_CATEGORIES = set(DEFAULT_WEIGHTS.keys())


def score_skill(category: str, base_score: float = 1.0) -> float:
    """
    Apply category weight to a base score.

    Args:
        category: Skill category name
        base_score: Raw score before weighting

    Returns:
        Weighted score
    """
    weight = DEFAULT_WEIGHTS.get(category, DEFAULT_WEIGHTS["other"])
    return base_score * weight
    from core.config import SCORING_WEIGHTS, PRECISION_LEVEL

def score_skill(category: str, base_score: float = 1.0) -> float:

    weight = SCORING_WEIGHTS.get(category, SCORING_WEIGHTS["other"])
    weighted_score = base_score * weight
    
    return round(weighted_score, PRECISION_LEVEL)


