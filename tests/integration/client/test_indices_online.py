def test_trading_rate_types(client):
    rate_types = client.indices_online.get_trading_rate_types()
    assert rate_types.get_index_trading_rate_types.total > 0
    assert len(rate_types.get_index_trading_rate_types.result) > 0


def test_intraday(client):
    intraday = client.indices_online.get_intraday(index_id=182)
    assert intraday.get_index_trading_data_intra_day.total >= 0
    # Note: result may be empty outside market hours


def test_last_rate_single(client):
    last_rate = client.indices_online.get_last_rate(index_id=182)
    # When filtering by index_id, result is a single object
    assert hasattr(last_rate.get_index_trading_data_intra_day, 'index_id')
    assert last_rate.get_index_trading_data_intra_day.index_id == 182


def test_last_rate_all(client):
    last_rate = client.indices_online.get_last_rate()
    # When getting all indices, result is an array
    assert isinstance(last_rate.get_index_trading_data_intra_day, list)
    assert len(last_rate.get_index_trading_data_intra_day) > 0