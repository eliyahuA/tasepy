import requests
import logging

from endpoints.factories.interfaces import IEndpointsFactory
from settings import Settings, SettingsBuilder
from bs4 import BeautifulSoup


class Client:

    def __init__(self,
                 settings: Settings,
                 endpoints_factory: IEndpointsFactory,
                 ):
        self.settings = settings
        self.endpoints = endpoints_factory.get_endpoints()

    def get_funds(self):
        url = f"{self.endpoints.base_url}/{self.endpoints.funds.group_url}/{self.endpoints.funds.funds_list.url}"
        params = {"listingStatusId": 1}
        headers = {
            'accept': "application/json",
            'accept-language': "he-IL",
            'apikey': f"{self.settings.api_key}"
        }

        response = requests.get(url, params=params, headers=headers)
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
    from models.endpoints import Endpoints

    client = Client(
        settings,
        YAMLFactory('./endpoints/endpoints.yaml', Endpoints),
    )

    funds = client.get_funds()
