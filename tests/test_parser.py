import pytest
from core.parser import normalize_text
from collections import Counter

def test_normalization_lowercasing():
    result = normalize_text("Python JAVA")
    assert "python" in result
    assert "java" in result

def test_technical_char_preservation():
    """CRITICAL: Ensure our new regex preserves tech-specific chars."""
    result = normalize_text("C++, CI/CD, and Node.js")
    assert "c++" in result
    assert "ci/cd" in result
    assert "node.js" in result

def test_gap_closing():
    """Ensure the parser handles sloppy human spacing."""
    result = normalize_text("CI / CD and node . js")
    assert "ci/cd" in result
    assert "node.js" in result
