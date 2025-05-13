import requests
import logging

from endpoints.factories.interfaces import IEndpointsFactory
from settings import Settings, SettingsBuilder
from bs4 import BeautifulSoup
from request_components import headers as headers
from request_components import parameters as parameters
from request_components import enums as enums

from typing import Optional


class Client:

    def __init__(self,
                 settings: Settings,
                 endpoints_factory: IEndpointsFactory,
                 accept_language: Optional[enums.AcceptLanguage] = None,
                 ):
        self.settings = settings
        self.endpoints = endpoints_factory.get_endpoints()
        self.accept_language = accept_language

    def get_funds(self, listing_status_id: Optional[enums] = None):
        url = f"{self.endpoints.base_url}/{self.endpoints.funds.group_url}/{self.endpoints.funds.funds_list.url}"
        params = parameters.FundList(listing_status_id=listing_status_id).model_dump()
        headers = {
            'accept': "application/json",
            'accept-language': "he-IL",
            'apikey': f"{self.settings.api_key}"
        }

        response = requests.get(
            url,
            params=params,
            headers=headers
        )

        if response.status_code != 200:
            raise RuntimeError(f"Request {url}, {params}, {headers} failed with status code {response.status_code}")
        response_string = response.content.decode('utf-8')
        if 'Request Rejected' in response_string:
            try:
                pretty_rejection = f"\n{BeautifulSoup(response_string, 'html.parser').prettify()}"
            except Exception as e:
                pretty_rejection = ''
            raise RuntimeError(f"Request {url}, {params}, {headers} was rejected{pretty_rejection}")
        return response.json()


if __name__ == '__main__':

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(filename)s:%(lineno)d | %(classname)s.%(funcName)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            # logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )

    settings = (SettingsBuilder()
                .with_apikey(file_path='./API key.yaml')
                .build())
    from endpoints.factories.yaml_factory import YAMLFactory
    from endpoints.factories.interfaces import IEndpointsFactory
    from request_components.urls import Endpoints

    client = Client(
        settings,
        YAMLFactory('./endpoints/endpoints.yaml', Endpoints),
    )

    funds = client.get_funds()
