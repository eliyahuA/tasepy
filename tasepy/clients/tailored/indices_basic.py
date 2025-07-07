import typeguard

from tasepy.responses import ForgivingResponse
from tasepy.responses.indices_basic import (
    IndicesList,
    IndexComponents
)
from .request_callable import APIRequestExecutor
from tasepy.requests_.parameters import BaseParameters
from tasepy.requests_.headers import LanguageAble
from tasepy.requests_.resources import DatedIndexResource
from .base_client import BaseClient
from typing import Optional, Tuple
from datetime import datetime


class IndicesBasic:
    """Domain specific client for TASE basic indices API endpoints.
    
    Provides methods to retrieve index lists and component information
    from the TASE DataWise API.
    """

    @typeguard.typechecked
    def __init__(self,
                 client: BaseClient,
                 request_callable: APIRequestExecutor,
                 ):
        """Initialize the IndicesBasic client.
        
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
                self.client.endpoints.indices,
                endpoint_url
            )

    @typeguard.typechecked
    def get_indices_list(self):
        """Get index list classifications for indices.
        
        Retrieves the available TASE indices with their identifiers,
        names, and ISIN codes for reference and selection.
        
        Returns:
            Indices list pydantic data model including list of index IDs, names, and ISIN codes
        """
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.indices.indices_list),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=IndicesList
        )

    @typeguard.typechecked
    def get_index_components(self, index_id: int, date: Tuple[int, int, int] | datetime):
        """Get index component data for a specific index and date.
        
        Retrieves the securities that compose a specific index on a given date,
        including security identifiers, symbols, and names.
        
        Args:
            index_id: Unique identifier of the index
            date: Date as either (day, month, year) tuple or datetime object
            
        Returns:
            Index components pydantic data model including list of securities with IDs, symbols, and names
            
        Raises:
            ValueError: If date is not a tuple or datetime object
        """
        if isinstance(date, Tuple):
            resource = DatedIndexResource(index_id=index_id, day=date[0], month=date[1], year=date[2])
        elif isinstance(date, datetime):
            resource = DatedIndexResource(index_id=index_id, year=date.year, month=date.month, day=date.day)
        else:
            raise ValueError("date must be either a Tuple or datetime")
        return self.request_callable(
            url=self._default_url_provider(self.client.endpoints.indices.index_components_basic),
            params=BaseParameters(),
            headers=self._default_header_provider(),
            response_model=IndexComponents,
            resource=resource
        )
