import re
from collections import Counter

def normalize_text(text: str) -> Counter:
    """
    Standardizes raw string input while preserving technical characters
    and closing common formatting gaps in tech terms.
    """
    if not text:
        return Counter()
    
    # 1. Lowercase
    text = text.lower()
    
    # 2. Pre-processing: Close gaps in common tech patterns
    # This turns "ci / cd" into "ci/cd" and "node . js" into "node.js"
    text = re.sub(r"\s+/\s+", "/", text)
    text = re.sub(r"\s+\.\s+", ".", text)
    
    # 3. Apply the 'Safe List' Regex
    # Added '.' to safe list to support things like 'node.js' or 'vue.js'
    text = re.sub(r"[^a-z0-9\s_+#/.]", " ", text)
    
    # 4. Final tokenization
    return Counter(text.split())
