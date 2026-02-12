import pytest
from core.ontology import load_ontology

def test_load_valid_ontology():
    """Ensure a known role returns a populated dictionary."""
    data = load_ontology("software_engineer")
    assert isinstance(data, dict)
    assert "python" in data

def test_load_invalid_ontology():
    """Ensure a non-existent role returns an empty dictionary, not an error."""
    data = load_ontology("underwater_basket_weaver")
    assert data == {}

def test_ontology_structure():
    """Verify that values in the JSON are valid weight categories."""
    data = load_ontology("software_engineer")
    # Added 'core_skill' and 'methodology' to match our new JSONs
    valid_categories = {"core_skill", "technical_skill", "soft_skill", "tool", "certification", "methodology", "other"}
    for category in data.values():
        assert category in valid_categories
