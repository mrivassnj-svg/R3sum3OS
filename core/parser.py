import re
from collections import Counter

def normalize_text(text: str) -> Counter:
    """
    Standardizes raw string input into a frequency-aware token map.
    Removes special characters and handles casing.
    """
    if not text:
        return Counter()
    
    # Lowercase and strip non-alphanumeric characters
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    
    return Counter(text.split())
