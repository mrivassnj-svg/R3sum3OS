from core.ontology import load_ontology


def test_load_ontology():
    ontology = load_ontology("software_engineer")
    assert isinstance(ontology, dict)
