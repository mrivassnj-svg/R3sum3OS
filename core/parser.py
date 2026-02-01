from collections import Counter
import re


def normalize_text(text: str) -> Counter:
    """
    Normalize text into frequency-aware tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return Counter(text.split())
from core.ontology_schema import OntologySchema
from collections import Counter
import re

def analyze_resume_keywords(data: dict):
    """
    Uses parser logic to find the most frequent terms 
    across all 'Experience' descriptions.
    """
    all_descriptions = " ".join([exp['description'] for exp in data.get('experience', [])])
    
    # Your parser logic
    tokens = normalize_text(all_descriptions)
    
    # Return the top 5 most mentioned technologies
    return tokens.most_common(5)
