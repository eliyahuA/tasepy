"""
    For production set environment variable TYPEGUARD_DISABLED=1 if you want to disable typeguard for better performance
"""
from clients.tailored.client import Client
from settings import SettingsBuilder
from endpoints.factories.yaml_factory import YAMLFactory
from requests_.urls import Endpoints
from pathlib import Path

if __name__ == "__main__":
    client = Client(
        SettingsBuilder()
        .with_apikey(file_path='./API KEY.yaml')
        .build(),
        YAMLFactory('./endpoints/endpoints.yaml', Endpoints)
    )
    types = client.funds.get_share_exposure_profiles()
    types.save_pretty_json(
        Path(r"C:\Users\eliya\source\repos\tasepy\tests\unit\responses\funds\samples\share-exposure-profile.json")
    )
