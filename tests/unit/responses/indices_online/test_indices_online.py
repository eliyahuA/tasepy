from tasepy.responses import indices_online
from ..common import custom_open
from functools import partial

custom_open = partial(custom_open, caller_path_string=__file__)


def test_trading_rate_types():
    with custom_open(json_name="trading-rate-types") as f:
        sample_json = f.read()
    model_instance = indices_online.TradingRateTypes.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, indices_online.TradingRateTypes)
    assert model_instance.get_index_trading_rate_types.total == 5
    assert len(model_instance.get_index_trading_rate_types.result) == 5
    
    # Check first item
    first_item = model_instance.get_index_trading_rate_types.result[0]
    assert first_item.index_trading_rate_type_id == "B"
    assert first_item.index_trading_rate_type_desc == "מדד בסיס"


def test_intraday():
    with custom_open(json_name="intraday-small") as f:
        sample_json = f.read()
    model_instance = indices_online.IntraDay.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, indices_online.IntraDay)
    assert model_instance.get_index_trading_data_intra_day.total == 3
    assert len(model_instance.get_index_trading_data_intra_day.result) == 3
    
    # Check first item (with nulls)
    first_item = model_instance.get_index_trading_data_intra_day.result[0]
    assert first_item.index_id == 166
    assert first_item.last_index_rate == 4388
    assert first_item.change is None
    assert first_item.last_sale_time is None
    assert first_item.index_trading_rate_type_id == "B"
    
    # Check second item (with values)
    second_item = model_instance.get_index_trading_data_intra_day.result[1]
    assert second_item.index_id == 709
    assert second_item.change == -0.01
    assert second_item.last_sale_time == "09:35:13"


def test_last_rate_multiple():
    with custom_open(json_name="last-rate-small") as f:
        sample_json = f.read()
    model_instance = indices_online.LastRate.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, indices_online.LastRate)
    assert isinstance(model_instance.get_index_trading_data_intra_day, list)
    assert len(model_instance.get_index_trading_data_intra_day) == 2
    
    # Check first item
    first_item = model_instance.get_index_trading_data_intra_day[0]
    assert first_item.index_id == 182
    assert first_item.last_index_rate == 1295.02
    assert first_item.change == 0
    assert first_item.last_sale_time == "17:24:21"
    assert first_item.index_trading_rate_type_id == "E"
    
    # Check second item
    second_item = model_instance.get_index_trading_data_intra_day[1]
    assert second_item.index_id == 183
    assert second_item.change == -1.13


def test_last_rate_single():
    with custom_open(json_name="last-rate-single-small") as f:
        sample_json = f.read()
    model_instance = indices_online.LastRate.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, indices_online.LastRate)
    assert not isinstance(model_instance.get_index_trading_data_intra_day, list)
    
    # Check single item
    item = model_instance.get_index_trading_data_intra_day
    assert item.index_id == 182
    assert item.last_index_rate == 1295.02
    assert item.change == 0
    assert item.last_sale_time == "17:24:21"
    assert item.index_trading_rate_type_id == "E"