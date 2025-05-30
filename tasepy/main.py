"""
    For production set environment variable TYPEGUARD_DISABLED=1 if you want to disable typeguard for better performance
"""
from clients.tailored.client import Client
from settings import SettingsBuilder
from endpoints.factories.yaml_factory import YAMLFactory
from requests_.urls import Endpoints

if __name__ == "__main__":
    client = Client(
        SettingsBuilder()
        .with_apikey(file_path='./API KEY.yaml')
        .build(),
        YAMLFactory('./endpoints/endpoints.yaml', Endpoints)
    )
    cep = client.funds.get_currency_exposure_profile()
    print(cep)
