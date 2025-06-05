import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from utils import clean_text


def test_clean_text():
    assert clean_text("  Bonjour   monde  ") == "Bonjour monde"
