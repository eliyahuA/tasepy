from typing import Optional


from tasepy.requests_ import enums as enums
from tasepy.responses import funds, ForgivingResponse
from .request_callable import APIRequestExecutor
from tasepy.requests_.parameters import BaseParameters, FundList
from tasepy.requests_.headers import LanguageAble
from .base_client import BaseClient
from tasepy.requests_.urls import Endpoint


class Funds:

    def __init__(self,
                 client: BaseClient,
                 request_callable: APIRequestExecutor,
                 ):
        self.request_callable = request_callable
        self.client = client
        # capture by reference to have the object instantiate with the client values at the moment of call
        self._default_header_provider = \
            lambda: LanguageAble(
                accept_language=self.client.accept_language,
                apikey=self.client.settings.api_key
            )
        self._default_url_provider = \
            lambda endpoint_url: (
                self.client.endpoints,
                self.client.endpoints.funds,
                endpoint_url
            )

    def get_funds(self, listing_status_id: Optional[enums] = None) -> funds.fund_list.FundList:
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.funds_list),
            params=FundList(listing_status_id=listing_status_id),
            headers=self._default_header_provider(),
            response_model=funds.fund_list.FundList
        )

    def get_currency_exposure_profiles(self):
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.currencies_exposure_profile),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.CurrencyExposure
        )

    def get_commissions(self):
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.distribution_commission),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.DistributionCommission
        )

    def get_types(self):
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.fund_types),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.FundType
            )

    def get_listing_statuses(self):
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.listing_status),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.ListingStatus
            )

    def get_mutual_fund_classifications(self):
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.classification),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.MutualFundClassification
            )

    def get_payment_policies(self):
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.payment_policy),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.PaymentPolicy
            )
