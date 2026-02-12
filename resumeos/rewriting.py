def rewrite_bullets(raw_text: str):
    bullets = [
        b.strip()
        for b in re.split(r'[\n•·*]', raw_text)
        if len(b.strip()) > 5
    ]

    refined = []
    for bullet in bullets:
        words = bullet.split()
        if not words: continue

        while words and words[0].lower() in WEAK_START_VERBS:
            words = words[1:]
        
        if not words: continue

        content_lower = " ".join(words).lower()
        
        # SQUEAKY CLEAN VARIABLE MATCHING
        if any(t in content_lower for t in ["python", "java", "sql", "aws", "docker"]):
            verb_pool = INTENT_VERBS["technical"]
        elif any(t in content_lower for t in ["data", "research", "test", "metric"]):
            verb_pool = INTENT_VERBS["analytical"]
        else:
            verb_pool = INTENT_VERBS["default"]

        verb = verb_pool[len(words) % len(verb_pool)]
        
        first_word = words[0]
        if not (first_word.isupper() or (len(first_word) > 1 and first_word[0].isupper())):
            words[0] = first_word.lower()

        content = " ".join(words)
        refined.append(f"{verb} {content}")

    return refined
