from typing import Optional


from tasepy.requests_ import enums as enums
from tasepy.responses import funds, ForgivingResponse
from .request_callable import APIRequestExecutor
from tasepy.requests_.parameters import BaseParameters, FundList
from tasepy.requests_.headers import LanguageAble
from .base_client import BaseClient


class Funds:
    """Client for TASE funds-related API endpoints.
    
    Provides methods to retrieve fund information, classifications, exposures,
    and other fund-related data from the TASE DataWise API.
    """

    def __init__(self,
                 client: BaseClient,
                 request_callable: APIRequestExecutor,
                 ):
        """Initialize the Funds client.
        
        Args:
            client: Base client containing settings and endpoint configuration
            request_callable: Function to execute API requests
        """
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
        """Retrieve list of available funds.
        
        Args:
            listing_status_id: Optional filter by listing status
            
        Returns:
            FundList containing fund information
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.funds_list),
            params=FundList(listing_status_id=listing_status_id),
            headers=self._default_header_provider(),
            response_model=funds.fund_list.FundList
        )

    def get_currency_exposure_profiles(self):
        """Get currency exposure profiles for funds.
        
        Returns:
            CurrencyExposure data for all funds
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.currencies_exposure_profile),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.CurrencyExposure
        )

    def get_commissions(self):
        """Get distribution commission information for funds.
        
        Returns:
            DistributionCommission data for all funds
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.distribution_commission),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.DistributionCommission
        )

    def get_types(self):
        """Get available fund types.
        
        Returns:
            FundType classifications
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.fund_types),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.FundType
            )

    def get_listing_statuses(self):
        """Get available listing statuses for funds.
        
        Returns:
            ListingStatus options
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.listing_status),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.ListingStatus
            )

    def get_mutual_fund_classifications(self):
        """Get mutual fund classification categories.
        
        Returns:
            MutualFundClassification data
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.classification),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.MutualFundClassification
            )

    def get_payment_policies(self):
        """Get available payment policies for funds.
        
        Returns:
            PaymentPolicy options
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.payment_policy),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.PaymentPolicy
            )

    def get_share_exposure_profiles(self):
        """Get share exposure profiles for funds.
        
        Returns:
            ShareExposureProfile data for all funds
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.shares_exposure_profile),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.ShareExposureProfile
            )

    def get_stock_exchanges(self):
        """Get available stock exchanges for fund trading.
        
        Returns:
            StockExchange information
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.stock_exchange),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.StockExchange
            )

    def get_tax_statuses(self):
        """Get available tax status categories for funds.
        
        Returns:
            TaxStatus classifications
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.tax_status),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.TaxStatus
            )

    def get_tracking_funds_classifications(self):
        """Get tracking fund classification categories.
        
        Returns:
            TrackingFundClassification data
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.tracking_fund_classification),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.TrackingFundClassification
        )

    def get_underlying_assets(self):
        """Get underlying asset types for funds.
        
        Returns:
            UnderlyingAsset classifications
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.underlying_assets),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.UnderlyingAsset
        )
