import sys
import site_checker

def test_tase_api_site(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['tase_api_site_checker','-url','https://datawise.tase.co.il/v1'])
        assert site_checker.main() == 200
