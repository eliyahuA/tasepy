from typing import Optional

from tasepy.settings import Settings
from tasepy.clients import tailored
from tasepy.requests_ import enums as enums
from tasepy.responses import funds
from .request_callable import RequestCallable
from tasepy.requests_.urls import Endpoints
from tasepy.requests_.parameters import BaseParameters, FundList
from tasepy.requests_.headers import CurrenciesExposureProfile, FundList


class Funds:

    def __init__(self,
                 settings: Settings,
                 request_callable: RequestCallable,
                 endpoints: Endpoints,
                 accept_language: Optional[enums.AcceptLanguage] = None):
        self.request_callable = request_callable
        self.endpoints = endpoints
        self.accept_language = accept_language
        self.settings = settings

    def get_funds(self, listing_status_id: Optional[enums] = None) -> funds.fund_list.FundList:
        return self.request_callable(
            url=(self.endpoints, self.endpoints.funds, self.endpoints.funds.funds_list),
            params=FundList(listing_status_id=listing_status_id),
            headers=FundList(accept_language=self.accept_language, apikey=self.settings.api_key),
            response_model=funds.fund_list.FundList
        )

    def get_currency_exposure_profile(self):
        return self.request_callable(
            url=(self.endpoints, self.endpoints.funds, self.endpoints.funds.currencies_exposure_profile),
            params=BaseParameters(),
            headers=CurrenciesExposureProfile(accept_language=self.accept_language, apikey=self.settings.api_key),
            response_model=funds.CurrencyExposure
        )