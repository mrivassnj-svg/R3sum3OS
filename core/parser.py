from collections import Counter
import re


def normalize_text(text: str) -> Counter:
    """
    Normalize text into frequency-aware tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return Counter(text.split())
