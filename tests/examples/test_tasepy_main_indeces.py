import sys
from tasepy.examples import tasepy_main_indices

def test_tase_api_site(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['tasepy_main_indices'])
        assert tasepy_main_indices.main() == 0
