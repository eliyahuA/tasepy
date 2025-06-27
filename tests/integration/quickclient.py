from tasepy import quick_client


def test_quick_client():
    client = quick_client()
    assert client is not None
