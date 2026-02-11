import time
from core.ontology_schema import OntologySchema, EntityType
from typing import List, Dict, Any

class ValidationResult:
    def __init__(self):
        self.is_valid = True
        self.errors = []
        self.warnings = []

    def add_error(self, message: str):
        self.is_valid = False
        self.errors.append(message)

def validate_ontology(data: Dict[str, Any]) -> ValidationResult:
    """
    The 'Kernel' utility to verify the integrity of the Resume Data.
    """
    result = ValidationResult()

    # 1. Root Structure Check
    required_root = ["identity", "experience", "skills"]
    for key in required_root:
        if key not in data:
            result.add_error(f"CRITICAL: Missing root sector '{key}'.")

    # 2. Entity Validation
    if "experience" in data:
        for idx, job in enumerate(data["experience"]):
            if not OntologySchema.validate_entity(job):
                result.add_error(f"Experience[{idx}] fails schema validation.")
            
            # --- INTEGRATED FIX START ---
            start = job.get('start_date')
            end = job.get('end_date')

            if start and end:
                # Handle 'Present' as current year to avoid string comparison errors
                current_year = str(time.localtime().tm_year)
                effective_end = current_year if str(end).lower() == "present" else end
                
                if effective_end < start:
                    result.add_error(f"Experience[{idx}]: Temporal paradox detected ({end} < {start}).")
            # --- INTEGRATED FIX END ---

    # 3. Relationship/Link Validation
    all_skill_ids = {s['id'] for s in data.get('skills', [])}
    for job in data.get('experience', []):
        for tech_id in job.get('technologies', []):
            if tech_id not in all_skill_ids:
                result.warnings.append(f"Broken Link: Job '{job['id']}' references unknown skill '{tech_id}'.")

    return result
