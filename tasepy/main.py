"""
    For production set environment variable TYPEGUARD_DISABLED=1 if you want to disable typeguard for better performance
"""
from clients.tailored.client import Client
from settings import SettingsBuilder
from endpoints.factories.yaml_factory import YAMLFactory
from requests_.urls import Endpoints
from pathlib import Path
from datetime import datetime, timedelta

if __name__ == "__main__":
    client = Client(
        SettingsBuilder()
        .with_apikey(file_path='./API KEY.yaml')
        .build(),
        YAMLFactory(Endpoints, './endpoints/endpoints.yaml')
    )
    types = client.indices_basic.get_index_components(182, datetime.now() - timedelta(days=30))
    types.save_pretty_json(
        Path(__file__).parent.parent / "tests/unit/responses/indices_basic/samples/components.json"
    )
