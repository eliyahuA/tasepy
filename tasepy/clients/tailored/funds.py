from typing import Optional


from tasepy.requests_ import enums as enums
from tasepy.responses import funds, ForgivingResponse
from .request_callable import APIRequestExecutor
from tasepy.requests_.parameters import BaseParameters, FundList
from tasepy.requests_.headers import LanguageAble
from .base_client import BaseClient


class Funds:
    """Domain specific client for TASE funds-related API endpoints.
    
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

    def get_funds(self, listing_status_id: Optional[enums.ListingStatusId] = None) -> funds.fund_list.FundList:
        """Retrieve list of available funds.
        
        Args:
            listing_status_id: Optional filter by listing status on omission default filter will be used
            
        Returns:
            FundList containing fund information for all filtered funds
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.funds_list),
            params=FundList(listing_status_id=listing_status_id),
            headers=self._default_header_provider(),
            response_model=funds.fund_list.FundList
        )

    def get_currency_exposure_profiles(self):
        """Get currency exposure profile classifications for funds.
        
        Retrieves the available currency exposure levels that categorize funds
        based on their foreign currency exposure as a percentage of net asset value.
        
        Returns:
            Currency exposure profile pydantic data model including list of exposure codes and descriptions
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.currencies_exposure_profile),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.CurrencyExposure
        )

    def get_commissions(self):
        """Get distribution commission classifications for funds.
        
        Retrieves the available distribution commission rates and types
        that categorize funds based on their distribution fee structure.
        
        Returns:
            Distribution commission pydantic data model including list of commission rates and types
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.distribution_commission),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.DistributionCommission
        )

    def get_types(self):
        """Get fund type classifications for funds.
        
        Retrieves the available fund types that categorize funds
        based on their structural and operational characteristics.
        
        Returns:
            Fund type pydantic data model including list of fund type codes and descriptions
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.fund_types),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.FundType
            )

    def get_listing_statuses(self):
        """Get listing status classifications for funds.
        
        Retrieves the available listing statuses that categorize funds
        based on their current trading and operational status.
        
        Returns:
            Listing status pydantic data model including list of status IDs and descriptions
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.listing_status),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.ListingStatus
            )

    def get_mutual_fund_classifications(self):
        """Get mutual fund classification categories for funds.
        
        Retrieves the hierarchical classification system that categorizes mutual funds
        by major, main, and secondary classification levels based on investment focus.
        
        Returns:
            Mutual fund classification pydantic data model including hierarchical classification structure with
            descriptions
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.classification),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.MutualFundClassification
            )

    def get_payment_policies(self):
        """Get payment policy classifications for funds.
        
        Retrieves the available payment policies that categorize funds
        based on their distribution and payment commitment schedules.
        
        Returns:
            Payment policy pydantic data model including list of policy codes and descriptions
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.payment_policy),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.PaymentPolicy
            )

    def get_share_exposure_profiles(self):
        """Get share exposure profile classifications for funds.
        
        Retrieves the available share exposure levels that categorize funds
        based on their equity share exposure as a percentage of net asset value.
        
        Returns:
            Share exposure profile pydantic data model including list of exposure codes and descriptions
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.shares_exposure_profile),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.ShareExposureProfile
            )

    def get_stock_exchanges(self):
        """Get stock exchange classifications for funds.
        
        Retrieves the available stock exchanges where foreign ETFs are traded,
        providing global exchange listings for fund investment tracking.
        
        Returns:
            Stock exchange pydantic data model including list of exchange codes and names
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.stock_exchange),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.StockExchange
            )

    def get_tax_statuses(self):
        """Get tax status classifications for funds.
        
        Retrieves the available tax status categories that classify funds
        based on their tax obligations and exemptions.
        
        Returns:
            Tax status pydantic data model including list of status codes and descriptions
        """
        return self.request_callable(
                url=self._default_url_provider(self.client.endpoints.funds.tax_status),
                params=BaseParameters(),
                headers=self._default_header_provider(),
                response_model=funds.TaxStatus
            )

    def get_tracking_funds_classifications(self):
        """Get tracking fund classification categories for funds.
        
        Retrieves the hierarchical classification system for tracking funds
        organized by major, main, and secondary classification levels.
        
        Returns:
            Tracking fund classification pydantic data model including hierarchical classification structure with
            descriptions
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.tracking_fund_classification),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.TrackingFundClassification
        )

    def get_underlying_assets(self):
        """Get underlying asset classifications for funds.
        
        Retrieves the available underlying assets and indices that funds track,
        including international indices, sector ETFs, and specific securities.
        
        Returns:
            Underlying asset pydantic data model including list of asset codes and descriptions
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.funds.underlying_assets),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=funds.UnderlyingAsset
        )
