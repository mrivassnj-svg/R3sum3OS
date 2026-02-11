"""
R3sum3OS - Configuration Registry
Centralized source of truth for scoring weights and precision.
"""

# Consolidated weights from both previous versions
SCORING_WEIGHTS = {
    "core_skill": 3.0,
    "technical_skill": 1.5,
    "tool": 2.0,
    "methodology": 1.5,
    "soft_skill": 1.0,
    "certification": 1.2,
    "other": 0.5
}

# Precision for rounding numeric results
PRECISION_LEVEL = 2
