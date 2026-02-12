import re

# Intent-based Verb Categories
INTENT_VERBS = {
    "technical": ["Engineered", "Implemented", "Developed", "Architected"],
    "analytical": ["Analyzed", "Optimized", "Researched", "Evaluated"],
    "leadership": ["Spearheaded", "Orchestrated", "Collaborated", "Mentored"],
    "default": ["Designed", "Automated", "Executed"]
}

WEAK_START_VERBS = {"made", "did", "worked", "helped", "used", "responsible", "i", "my", "was"}

def rewrite_bullets(raw_text: str):
    # Improved regex: split by newline, bullets, or multiple spaces
    bullets = [
        b.strip()
        for b in re.split(r'[\n•·*]', raw_text)
        if len(b.strip()) > 5
    ]

    refined = []
    for bullet in bullets:
        words = bullet.split()
        if not words: continue

        # 1. Strip the "Weak" start
        while words and words[0].lower() in WEAK_START_VERBS:
            words = words[1:]
        
        if not words: continue

        # 2. Semantic Intent Check
        # Does the bullet contain tech keywords?
        content_lower = " ".join(words).lower()
        
        if any(tech in content_lower for tech in ["python", "java", "sql", "aws", "docker"]):
            verb_pool = INTENT_VERBS["technical"]
        elif any(anal in content_lower for tech in ["data", "research", "test", "metric"]):
            verb_pool = INTENT_VERBS["analytical"]
        else:
            verb_pool = INTENT_VERBS["default"]

        # Select a verb based on length to keep it consistent but varied
        verb = verb_pool[len(words) % len(verb_pool)]
        
        # 3. Capitalization Shield
        # Only lowercase the next word if it's NOT a proper noun (all caps or Title Case)
        first_word = words[0]
        if not (first_word.isupper() or (len(first_word) > 1 and first_word[0].isupper())):
            words[0] = first_word.lower()

        content = " ".join(words)
        refined.append(f"{verb} {content}")

    return refined
