from tasepy.responses import funds
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def custom_open(json_name):
    with open(Path(__file__).parent / 'samples' / f"{json_name}.json", 'r', encoding='utf-8') as f:
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


def test_mutual_fund_classification():
    with custom_open("mutual-fund-classification") as f:
        sample_json = f.read()
    model_instance = funds.MutualFundClassification.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.MutualFundClassification)
    assert model_instance.fund_classification.total > 0


def test_payment_policy():
    with custom_open("payment-policy") as f:
        sample_json = f.read()
    model_instance = funds.PaymentPolicy.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.PaymentPolicy)
    assert model_instance.payment_policy.total > 0


def test_share_exposure():
    with custom_open("share-exposure-profile") as f:
        sample_json = f.read()
    model_instance = funds.ShareExposureProfile.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.ShareExposureProfile)
    assert model_instance.share_exposure_profile.total > 0


def test_stock_exchange():
    with custom_open("stock-exchange") as f:
        sample_json = f.read()
    model_instance = funds.StockExchange.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.StockExchange)
    assert model_instance.foreign_etf_stock_exchange.total > 0


def test_tax_status():
    with custom_open("tax-status") as f:
        sample_json = f.read()
    model_instance = funds.TaxStatus.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.TaxStatus)
    assert model_instance.tax_status.total > 0


def test_tracking_fund_classification():
    with custom_open("tracking-fund-classification") as f:
        sample_json = f.read()
    model_instance = funds.TrackingFundClassification.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.TrackingFundClassification)
    assert model_instance.fund_classification.total > 0


def test_underlying_asset():
    with custom_open("underlying-asset") as f:
        sample_json = f.read()
    model_instance = funds.UnderlyingAsset.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, funds.UnderlyingAsset)
    assert model_instance.underlying_asset.total > 0
