"""
Ontology loader for job-specific skill mappings.
"""

import json
from pathlib import Path
from typing import Dict


def load_ontology(job_role: str) -> Dict[str, str]:
    """
    Loads ontology JSON based on job role.
    """
    path = Path("ontology") / f"{job_role}.json"

    if not path.exists():
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
