from core.ontology_schema import OntologySchema
from core.parser import normalize_text
from typing import List, Tuple

def analyze_resume_keywords(data: dict, top_n: int = 5) -> List[Tuple[str, int]]:
    """
    Orchestrates the extraction of frequency data from the 'Experience' 
    section of the resume data.
    """
    # Extract descriptions safely using the schema's expected structure
    experiences = data.get('experience', [])
    
    # Combine all prose into one string for analysis
    all_descriptions = " ".join([
        exp.get('description', '') for exp in experiences
    ])
    
    # Use the parser to get counts
    tokens = normalize_text(all_descriptions)
    
    # Return the most frequent terms (useful for 'Skills' visualization)
    return tokens.most_common(top_n)
