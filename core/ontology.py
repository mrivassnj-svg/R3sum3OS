import json
from pathlib import Path
from typing import Dict

def load_ontology(job_role: str) -> Dict[str, any]:
    """
    Loads ontology JSON based on job role.
    """
    path = Path("ontology") / f"{job_role}.json"

    if not path.exists():
        print(f"Warning: Ontology for {job_role} not found at {path}")
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in {path}")
        return {}
