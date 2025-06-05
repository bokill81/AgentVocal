import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from prompts import PHASES

def test_has_introduction_phase():
    assert "introduction" in PHASES
