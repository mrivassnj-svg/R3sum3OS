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
    if not raw_text:
        return []

    # 1. Cleanly split and filter bullets
    # Use re directly here - ensure no spaces before 'import re' at top of file
    try:
        bullets = [
            b.strip()
            for b in re.split(r'[\n•·*]', raw_text)
            if len(b.strip()) > 5
        ]
    except NameError:
        # Emergency fallback if re fails for some bizarre environment reason
        bullets = [b.strip() for b in raw_text.split('\n') if len(b.strip()) > 5]

    refined = []
    for bullet in bullets:
        words = bullet.split()
        if not words: continue

        # Strip "Weak" starts
        while words and words[0].lower() in WEAK_START_VERBS:
            words = words[1:]
        
        if not words: continue

        content_lower = " ".join(words).lower()
        
        # 2. Semantic Intent Check (Variables matched: 't' in both places)
        if any(t in content_lower for t in ["python", "java", "sql", "aws", "docker", "c++", "linux"]):
            verb_pool = INTENT_VERBS["technical"]
        elif any(t in content_lower for t in ["data", "research", "test", "metric", "analyze"]):
            verb_pool = INTENT_VERBS["analytical"]
        else:
            verb_pool = INTENT_VERBS["default"]

        # Select a consistent verb
        verb = verb_pool[len(words) % len(verb_pool)]
        
        # 3. Capitalization Shield
        first_word = words[0]
        if not (first_word.isupper() or (len(first_word) > 1 and first_word[0].isupper())):
            words[0] = first_word.lower()

        content = " ".join(words)
        refined.append(f"{verb} {content}")

    return refined
