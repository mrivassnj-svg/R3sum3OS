import pytest
from collections import Counter

@pytest.fixture
def sample_ontology():
    return {
        "python": "core_skill",      # Upgraded from technical_skill
        "agile": "methodology",      # New category
        "docker": "tool",
        "communication": "soft_skill"
    }

@pytest.fixture
def sample_jd_text():
    return "Looking for a Python expert with Docker and Agile experience."

@pytest.fixture
def sample_resume_text():
    return "Expert in Python and Docker."
