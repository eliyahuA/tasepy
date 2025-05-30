from typing import Optional


from tasepy.requests_ import enums as enums
from tasepy.responses import funds
from .request_callable import APIRequestExecutor
from tasepy.requests_.parameters import BaseParameters, FundList
from tasepy.requests_.headers import CurrenciesExposureProfile, FundList
from .base_client import BaseClient


class Funds:

    def __init__(self,
                 client: BaseClient,
                 request_callable: APIRequestExecutor,
                 ):
        self.request_callable = request_callable
        self.client = client

    def get_funds(self, listing_status_id: Optional[enums] = None) -> funds.fund_list.FundList:
        return self.request_callable(
            url=(self.client.endpoints, self.client.endpoints.funds, self.client.endpoints.funds.funds_list),
            params=FundList(listing_status_id=listing_status_id),
            headers=FundList(accept_language=self.client.accept_language, apikey=self.client.settings.api_key),
            response_model=funds.fund_list.FundList
        )

    def get_currency_exposure_profile(self):
        return self.request_callable(
            url=(self.client.endpoints,
                 self.client.endpoints.funds,
                 self.client.endpoints.funds.currencies_exposure_profile
                 ),
            params=BaseParameters(),
            headers=CurrenciesExposureProfile(
                accept_language=self.client.accept_language,
                apikey=self.client.settings.api_key
            ),
            response_model=funds.CurrencyExposure
        )
