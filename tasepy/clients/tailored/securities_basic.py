import typeguard

from tasepy.responses import ForgivingResponse
from tasepy.responses.securities_basic.companies_list import CompaniesList
from .request_callable import APIRequestExecutor
from tasepy.requests_.parameters import BaseParameters
from tasepy.requests_.headers import LanguageAble
from tasepy.requests_.resources import DatedResource, MonthlyDatedResource, NoResource
from .base_client import BaseClient


class SecuritiesBasic:
    """Domain specific client for TASE basic securities API endpoints.
    
    Provides methods to retrieve securities lists, company information, and trading data
    from the TASE DataWise API.
    """

    @typeguard.typechecked
    def __init__(self,
                 client: BaseClient,
                 request_callable: APIRequestExecutor,
                 ):
        """Initialize the SecuritiesBasic client.
        
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
                self.client.endpoints.securities,
                endpoint_url
            )

    @typeguard.typechecked
    def get_trade_securities_list(self, year: int, month: int, day: int):
        """Get traded securities list for a specific date.
        
        Retrieves extensive current and historical data for the list of issuers
        and securities traded on the Tel Aviv Stock Exchange for the specified date.
        
        Args:
            year: Specific year (1999-2030)
            month: Specific month (1-12)
            day: Specific day (1-31)
            
        Returns:

        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.securities.trade_securities_list),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=ForgivingResponse,
            resource=DatedResource(year=year, month=month, day=day)
        )

    @typeguard.typechecked
    def get_delisted_securities_list(self, year: int, month: int):
        """Get delisted securities list for a specific year and month.
        
        Retrieves a list of securities that have been delisted from the Tel Aviv 
        Stock Exchange during the specified year and month period.
        
        Args:
            year: Specific year (1999-2030)
            month: Specific month (1-12)
            
        Returns:

        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.securities.delisted_securities_list),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=ForgivingResponse,
            resource=MonthlyDatedResource(year=year, month=month)
        )

    @typeguard.typechecked
    def get_companies_list(self):
        """Get companies list for securities.
        
        Retrieves a list of the companies listed on the Tel Aviv Stock Exchange
        providing comprehensive company information and identifiers.
        
        Returns:
            CompaniesList: Pydantic data model containing company information including 
            company names, TASE sectors, issuer IDs, corporate IDs, and dual listing status
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.securities.companies_list),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=CompaniesList
        )

    @typeguard.typechecked
    def get_illiquid_maintenance_suspension_list(self):
        """Get illiquid maintenance and suspension list for securities.
        
        Retrieves the maintenance, suspension and illiquid securities lists for the 
        securities traded on the Tel Aviv Stock Exchange for the next trading day.
        
        Returns:

        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.securities.illiquid_maintenance_suspension_list),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=ForgivingResponse
        )

    @typeguard.typechecked
    def get_trading_code_list(self):
        """Get trading code list for securities.
        
        Retrieves the trading codes' list of the Tel Aviv Stock Exchange
        providing reference codes used for securities trading operations.
        
        Returns:

        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.securities.trading_code_list),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=ForgivingResponse
        )

    @typeguard.typechecked
    def get_securities_types(self):
        """Get securities types classifications for securities.
        
        Retrieves the types of securities traded on the Tel Aviv Stock Exchange
        providing classification categories for different security instruments.
        
        Returns:

        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.securities.securities_types),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=ForgivingResponse
        )