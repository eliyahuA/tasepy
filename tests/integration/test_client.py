import tasepy

from tasepy.settings import SettingsBuilder
from tasepy.endpoints.factories.yaml_factory import YAMLFactory
from tasepy.clients.tailored import Client
from pathlib import Path
from importlib import resources
from pytest import fixture
from tasepy.requests_.urls import Endpoints
from dotenv import load_dotenv

load_dotenv()


@fixture()
def settings():
    return (SettingsBuilder()
            .with_apikey(environment="API_KEY")
            .build())


@fixture()
def url_model_factory():
    return YAMLFactory(Path(str(resources.files(tasepy))) / 'endpoints' / 'endpoints.yaml', Endpoints)


@fixture()
def client(settings, url_model_factory):
    return Client(settings, url_model_factory)


def test_funds_list(client):
    funds = client.funds.get_funds()
    assert funds.funds.total > 0


def test_currency_exposure_profile(client):
    currency_exposure = client.funds.get_currency_exposure_profiles()
    assert currency_exposure.currency_exposure_profile.total > 0


def test_distribution_commission(client):
    commissions = client.funds.get_commissions()
    assert commissions.distribution_commission.total > 0
