import pytest
from core.parser import normalize_text
from collections import Counter

def test_normalization_lowercasing():
    """Ensure text is converted to lowercase."""
    result = normalize_text("Python JAVA")
    assert "python" in result
    assert "java" in result
    assert "Python" not in result

def test_punctuation_removal():
    """Ensure special characters are stripped out."""
    result = normalize_text("Python/Django, React!")
    # Counter keys should be clean
    assert "python" in result
    assert "django" in result
    assert "react" in result

def test_empty_input():
    """Ensure the parser handles empty strings without crashing."""
    result = normalize_text("")
    assert isinstance(result, Counter)
    assert len(result) == 0

def test_stopword_filtering():
    """Verify that common words are excluded from the count."""
    result = normalize_text("Python and the Java")
    assert "and" not in result
    assert "the" not in result
