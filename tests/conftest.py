# tests/conftest.py
import pytest
from collections import Counter

@pytest.fixture
def sample_ontology():
    return {
        "python": "technical_skill",
        "sql": "technical_skill",
        "docker": "tool",
        "communication": "soft_skill"
    }

@pytest.fixture
def sample_jd():
    return Counter(["python", "sql", "docker", "communication"])

@pytest.fixture
def sample_resume():
    return Counter(["python", "docker"])
