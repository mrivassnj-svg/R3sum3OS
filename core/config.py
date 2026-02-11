"""
R3sum3OS Configuration Registry
Centralized Named Constants for Scoring and Logic.
"""

# 2.6 Named Constants (Global weights)
# These represent the "exchange rate" for different skill types
SCORING_WEIGHTS = {
    "technical_skill": 1.5,
    "core_skill": 3.0,      # High priority for job matching
    "tool": 2.0,            # Standard proficiency
    "methodology": 1.5,     # Process-oriented skills
    "soft_skill": 1.0,      # Foundational skills
    "certification": 1.2,   # Added value
    "other": 0.5            # Default fallback
}

# 2.11 Rounding Precision
PRECISION_LEVEL = 2
