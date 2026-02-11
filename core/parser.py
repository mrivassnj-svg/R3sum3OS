import re
from collections import Counter

def normalize_text(text: str) -> Counter:
    """
    Standardizes raw string input while preserving technical characters.
    """
    if not text:
        return Counter()
    
    # Lowercase first
    text = text.lower()
    
    # NEW REGEX: Preserve underscores, pluses (C++), and hashes (C#)
    # This allows 'system_design' and 'c++' to remain intact
    text = re.sub(r"[^a-z0-9\s_+#]", " ", text)
    
    # Split handles multiple spaces automatically
    return Counter(text.split())
