"""
Defines and applies weighting rules for resume scoring.
"""

from typing import Dict
from core.config import SCORING_WEIGHTS, PRECISION_LEVEL

def score_skill(category: str, base_score: float = 1.0) -> float:
    """
    Apply category weight to a base score using the central registry.

    Args:
        category: Skill category name (e.g., 'core_skill', 'tool')
        base_score: Raw score before weighting

    Returns:
        Weighted score rounded to defined precision
    }
    """
    # Fetch weight from config, defaulting to 'other' if category is missing
    weight = SCORING_WEIGHTS.get(category, SCORING_WEIGHTS["other"])
    
    weighted_score = base_score * weight
    
    return round(weighted_score, PRECISION_LEVEL)
