from core.parser import normalize_text


def test_normalize_text():
    tokens = normalize_text("Python, Python! SQL.")
    assert tokens["python"] == 2
    assert tokens["sql"] == 1
