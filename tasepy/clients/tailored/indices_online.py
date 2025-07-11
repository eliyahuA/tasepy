from typing import Optional

from tasepy.responses import ForgivingResponse
from tasepy.responses.indices_online import TradingRateTypes, IntraDay, LastRate
from .request_callable import APIRequestExecutor
from tasepy.requests_.parameters import BaseParameters, IntradayParameters, LastRateParameters
from tasepy.requests_.headers import LanguageAble
from .base_client import BaseClient


class IndicesOnline:
    """Domain specific client for TASE online indices API endpoints.
    
    Provides methods to retrieve real-time indices data including intraday rates,
    last rates, and trading rate types from the TASE DataWise API.
    """

    def __init__(self,
                 client: BaseClient,
                 request_callable: APIRequestExecutor,
                 ):
        """Initialize the IndicesOnline client.
        
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
                self.client.endpoints.indices_online,
                endpoint_url
            )

    def get_intraday(self, index_id: Optional[int] = None, start_time: Optional[str] = None) -> IntraDay:
        """Get intraday index prices for online indices.
        
        Retrieves intraday index price data with timestamps, rate changes,
        and trading rate type classifications for real-time monitoring.
        
        Args:
            index_id: Optional filter by specific index ID
            start_time: Optional start time filter in HH:mm:ss format
            
        Returns:
            Intraday index data pydantic model including timestamps, rates, changes, and trading types
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.indices_online.intraday),
            params=IntradayParameters(index_id=index_id, start_time=start_time),
            headers=self._default_header_provider(),
            response_model=IntraDay
        )

    def get_last_rate(self, index_id: Optional[int] = None) -> LastRate:
        """Get latest price updates for online indices.
        
        Retrieves the most recent index price updates with current rates,
        changes, and trading timestamps for real-time monitoring.
        
        Args:
            index_id: Optional filter by specific index ID
            
        Returns:
            Last rate index data pydantic model including current rates, changes, and timestamps
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.indices_online.last_rate),
            params=LastRateParameters(index_id=index_id),
            headers=self._default_header_provider(),
            response_model=LastRate
        )

    def get_trading_rate_types(self) -> TradingRateTypes:
        """Get index trading rate type classifications.
        
        Retrieves the available index trading rate types that categorize indices
        based on their trading phases and rate calculation methods.
        
        Returns:
            Trading rate types pydantic data model including list of type IDs and descriptions
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.indices_online.trading_rate_types),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=TradingRateTypes
        )