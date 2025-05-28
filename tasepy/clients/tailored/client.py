import requests

from bs4 import BeautifulSoup
from tasepy.endpoints.factories.interfaces import IEndpointsFactory
from tasepy.responses import ResponseComponent
from tasepy.settings import Settings
from tasepy import responses
from tasepy.requests_ import headers as head
from tasepy.requests_ import parameters as parameters
from tasepy.requests_ import enums as enums
from tasepy.requests_.urls import Endpoints, EndpointGroup, Endpoint
from typing import Optional, Tuple, Type, TypeVar

T = TypeVar('T', bound=ResponseComponent)


class Client:

    def __init__(self,
                 settings: Settings,
                 endpoints_model_factory: IEndpointsFactory[Endpoints],
                 accept_language: Optional[enums.AcceptLanguage] = None,
                 ):
        self.settings = settings
        self.endpoints = endpoints_model_factory.get_endpoints()
        self.accept_language = accept_language

    @staticmethod
    def _do_request(
            url: Tuple[Endpoints, EndpointGroup, Endpoint],
            params: parameters.BaseParameters,
            headers: head.Header,
            response_model: Type[T]
    ) -> T:
        _url = f"{url[0].base_url}/{url[1].group_url}/{url[2].url}"
        _params = params.model_dump()
        response = requests.get(
            url=_url,
            params=_params,
            headers=headers.model_dump(),
        )

        if response.status_code != 200:
            raise RuntimeError(f"Request {_url}, {_params}, {headers.model_dump(mask=True)} "
                               f"failed with status code {response.status_code}")
        response_string = response.text
        if 'Request Rejected' in response_string:
            try:
                pretty_rejection = f"\n{BeautifulSoup(response_string, 'html.parser').prettify()}"
            except Exception as e:
                pretty_rejection = ''
            raise RuntimeError(f"Request {_url}, {_params}, {headers.model_dump(mask=True)} "
                               f"was rejected{pretty_rejection}")

        return response_model.model_validate_json(response_string)

    def get_funds(self, listing_status_id: Optional[enums] = None) -> responses.funds.fund_list.FundList:
        return self._do_request(
            url=(self.endpoints, self.endpoints.funds, self.endpoints.funds.funds_list),
            params=parameters.FundList(listing_status_id=listing_status_id),
            headers=head.FundList(accept_language=self.accept_language, apikey=self.settings.api_key),
            response_model=responses.funds.fund_list.FundList
        )

    def get_currency_exposure_profile(self):
        return self._do_request(
            url=(self.endpoints, self.endpoints.funds, self.endpoints.funds.currencies_exposure_profile),
            params=parameters.BaseParameters(),
            headers=head.CurrenciesExposureProfile(accept_language=self.accept_language, apikey=self.settings.api_key),
            response_model=responses.ForgivingResponse
        )


if __name__ == '__main__':
    pass
