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
    return YAMLFactory(Endpoints, Path(str(resources.files(tasepy))) / 'endpoints' / 'endpoints.yaml')


@fixture()
def client(settings, url_model_factory):
    return Client(settings, url_model_factory)
