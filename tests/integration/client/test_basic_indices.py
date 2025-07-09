from datetime import datetime, timedelta


def test_indices_list(client):
    indices = client.indices_basic.get_indices_list()
    assert indices.indices_list.total > 0


def test_index_components(client):
    indices = client.indices_basic.get_index_components(182, datetime.now() - timedelta(days=30))
    assert indices.index_components.total > 0
