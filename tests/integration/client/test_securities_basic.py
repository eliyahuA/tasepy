from datetime import datetime, timedelta


def test_companies_list(client):
    companies = client.securities_basic.get_companies_list()
    assert companies.companies_list.total > 0


def test_securities_types(client):
    securities_types = client.securities_basic.get_securities_types()
    assert securities_types.securities_types.total > 0


def test_trading_code_list(client):
    trading_codes = client.securities_basic.get_trading_code_list()
    assert trading_codes.trading_list_code.total > 0


def test_illiquid_maintenance_suspension_list(client):
    illiquid_list = client.securities_basic.get_illiquid_maintenance_suspension_list()
    assert len(illiquid_list.illiquid_maintenance_and_suspension_list.result) >= 0


def test_delisted_securities_list(client):
    recent_date = datetime.now() - timedelta(days=30)
    delisted_securities = client.securities_basic.get_delisted_securities_list(recent_date.year, recent_date.month)
    assert len(delisted_securities.delisted_securities_list.result) >= 0


def test_trade_securities_list(client):
    recent_date = datetime.now() - timedelta(days=30)
    trade_securities = client.securities_basic.get_trade_securities_list(
        recent_date.year,
        recent_date.month,
        recent_date.day
    )
    assert trade_securities.trade_securities_list.total > 0
