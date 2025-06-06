
def test_funds_list(client):
    funds = client.funds.get_funds()
    assert funds.funds.total > 0


def test_currency_exposure_profile(client):
    currency_exposure = client.funds.get_currency_exposure_profiles()
    assert currency_exposure.currency_exposure_profile.total > 0


def test_distribution_commissions(client):
    commissions = client.funds.get_commissions()
    assert commissions.distribution_commission.total > 0


def test_fund_types(client):
    types = client.funds.get_types()
    assert types.fund_type.total > 0


def test_listing_statuses(client):
    listing_statuses = client.funds.get_listing_statuses()
    assert len(listing_statuses.listing_status.result) > 0


def test_mutual_fund_classifications(client):
    classifications = client.funds.get_mutual_fund_classifications()
    assert classifications.fund_classification.total > 0


def test_payment_policies(client):
    policies = client.funds.get_payment_policies()
    assert policies.payment_policy.total > 0


def test_share_exposure_profiles(client):
    share_exposure = client.funds.get_share_exposure_profiles()
    assert share_exposure.share_exposure_profile.total > 0


def test_stock_exchanges(client):
    share_exposure = client.funds.get_stock_exchanges()
    assert share_exposure.foreign_etf_stock_exchange.total > 0


def test_tax_statuses(client):
    tax_statuses = client.funds.get_tax_statuses()
    assert tax_statuses.tax_status.total > 0


def test_tracking_funds_classifications(client):
    classifications = client.funds.get_tracking_funds_classifications()
    assert classifications.fund_classification.total > 0


def test_underlying_assets(client):
    classifications = client.funds.get_underlying_assets()
    assert classifications.underlying_asset.total > 0
