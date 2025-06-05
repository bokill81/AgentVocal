import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import importlib
import pytest

MODULES = ["ia", "tts", "stt", "prompts", "config", "call", "log", "utils"]

@pytest.mark.parametrize("module", MODULES)
def test_import(module):
    try:
        importlib.import_module(module)
    except ModuleNotFoundError as e:
        pytest.skip(f"module {module} missing dependency: {e}")
