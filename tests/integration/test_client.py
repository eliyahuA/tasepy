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


def test_funds_list(settings, url_model_factory):

    client = Client(
        settings,
        url_model_factory
    )

    funds = client.get_funds()
    assert funds.funds.total > 0


def test_currency_exposure_profile(settings, url_model_factory):
    client = Client(
        settings,
        url_model_factory
    )

    currency_exposure = client.get_currency_exposure_profile()
    assert currency_exposure.total > 0
