import re

ACTION_VERBS = [
    "Designed","Implemented","Developed",
    "Analyzed","Optimized","Automated","Engineered"
]

WEAK_START_VERBS = {
    "made","did","worked","helped","used","responsible","i","my"
}

def rewrite_bullets(raw_text: str):
    bullets = [
        b.strip()
        for b in re.split(r'[\n•·*]', raw_text)
        if len(b.strip()) > 5
    ]

    refined = []
    for i, bullet in enumerate(bullets):
        words = bullet.split()
        if not words:
            continue

        if words[0].lower() in WEAK_START_VERBS:
            words = words[1:]

        if not words:
            continue

        verb = ACTION_VERBS[i % len(ACTION_VERBS)]
        content = " ".join(words)
        refined.append(f"{verb} {content[0].lower() + content[1:]}")

    return refined
