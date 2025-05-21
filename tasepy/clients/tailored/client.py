import requests
from tasepy import responses
import logging

from tasepy.endpoints.factories.interfaces import IEndpointsFactory
from tasepy.settings import Settings, SettingsBuilder
from bs4 import BeautifulSoup
from tasepy.requests_ import headers as head
from tasepy.requests_ import parameters as parameters
from tasepy.requests_ import enums as enums

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

    def get_funds(self, listing_status_id: Optional[enums] = None) -> responses.funds.fund_list.FundList:
        url = f"{self.endpoints.base_url}/{self.endpoints.funds.group_url}/{self.endpoints.funds.funds_list.url}"
        params = parameters.FundList(listing_status_id=listing_status_id).model_dump()
        headers = head.FundList(accept_language=self.accept_language, apikey=self.settings.api_key).model_dump()

        response = requests.get(
            url,
            params=params,
            headers=headers
        )

        if response.status_code != 200:
            raise RuntimeError(f"Request {url}, {params}, {headers} failed with status code {response.status_code}")
        response_string = response.text
        if 'Request Rejected' in response_string:
            try:
                pretty_rejection = f"\n{BeautifulSoup(response_string, 'html.parser').prettify()}"
            except Exception as e:
                pretty_rejection = ''
            raise RuntimeError(f"Request {url}, {params}, {headers} was rejected{pretty_rejection}")

        return responses.funds.fund_list.FundList.model_validate_json(response_string)


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
    from tasepy.endpoints.factories.yaml_factory import YAMLFactory
    from tasepy.endpoints.factories.interfaces import IEndpointsFactory
    from tasepy.requests_.urls import Endpoints

    client = Client(
        settings,
        YAMLFactory('./endpoints/endpoints.yaml', Endpoints),
    )

    funds = client.get_funds()
    print(funds)