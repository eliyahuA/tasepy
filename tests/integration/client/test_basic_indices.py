
def test_indices_list(client):
    indices = client.indices_basic.get_indices_list()
    assert indices.indices_list.total > 0

