from tasepy.responses import securities_basic
from ..common import custom_open
from functools import partial

custom_open = partial(custom_open, caller_path_string=__file__)


def test_companies_list():
    with custom_open(json_name="companies-list") as f:
        sample_json = f.read()
    model_instance = securities_basic.CompaniesList.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, securities_basic.CompaniesList)


def test_securities_types():
    with custom_open(json_name="securities-types") as f:
        sample_json = f.read()
    model_instance = securities_basic.SecuritiesTypes.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, securities_basic.SecuritiesTypes)


def test_trading_code_list():
    with custom_open(json_name="trading-code-list") as f:
        sample_json = f.read()
    model_instance = securities_basic.TradingCodeList.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, securities_basic.TradingCodeList)


def test_illiquid_maintenance_suspension_list():
    with custom_open(json_name="illiquid-maintenance-suspension-list") as f:
        sample_json = f.read()
    model_instance = securities_basic.IlliquidMaintenanceSuspensionList.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, securities_basic.IlliquidMaintenanceSuspensionList)


def test_delisted_securities_list():
    with custom_open(json_name="delisted-securities-list") as f:
        sample_json = f.read()
    model_instance = securities_basic.DelistedSecuritiesList.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, securities_basic.DelistedSecuritiesList)


def test_trade_securities_list():
    with custom_open(json_name="trade-securities-list") as f:
        sample_json = f.read()
    model_instance = securities_basic.TradeSecuritiesList.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, securities_basic.TradeSecuritiesList)