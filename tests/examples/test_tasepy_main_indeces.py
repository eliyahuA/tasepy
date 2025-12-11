import sys
from tasepy.examples import tasepy_main_indices

def test_tasepy_main_indices(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['tasepy_main_indices'])
        assert tasepy_main_indices.main() == 0
