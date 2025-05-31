from tasepy.responses import funds
from contextlib import contextmanager


@contextmanager
def custom_open(json_name):
    with open(f"./samples/{json_name}.json", 'r', encoding='utf-8') as f:
        yield f


def test_fund_list():
    with custom_open("fund-list") as f:
        sample_json = f.read()
    model_instance = funds.FundList.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.FundList)


def test_currency_exposure():
    with custom_open("currency-exposure-profile") as f:
        sample_json = f.read()
    model_instance = funds.CurrencyExposure.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.CurrencyExposure)


def test_distribution_commission():
    with custom_open("distribution-commission") as f:
        sample_json = f.read()
    model_instance = funds.DistributionCommission.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.DistributionCommission)


def test_fund_types():
    with custom_open("fund-types") as f:
        sample_json = f.read()
    model_instance = funds.FundType.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.FundType)


def test_listing_statuses():
    with custom_open("listing-statuses") as f:
        sample_json = f.read()
    model_instance = funds.ListingStatus.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.ListingStatus)
