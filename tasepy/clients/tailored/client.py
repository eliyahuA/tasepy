import requests

from bs4 import BeautifulSoup

from tasepy.endpoints.factories.interfaces import IEndpointsFactory
from tasepy.responses import ResponseComponent
from tasepy.settings import Settings
from tasepy.requests_ import headers as head
from tasepy.requests_ import parameters as parameters
from tasepy.requests_ import enums as enums
from tasepy.requests_.urls import Endpoints, EndpointGroup, Endpoint
from tasepy.requests_.resources import IResource, NoResource

from typing import Optional, Tuple, Type, TypeVar
from .funds import Funds
from .indices_basic import IndicesBasic
from .indices_online import IndicesOnline
from .securities_basic import SecuritiesBasic
from .base_client import BaseClient

T = TypeVar('T', bound=ResponseComponent)


class Client(BaseClient):
    """Main client for TASE DataWise API interactions.
    
    Provides high-level access to all TASE API endpoints through specialized
    domain clients (funds, indices_basic, indices_online, securities_basic). Handles request execution, response
    parsing, and error handling.
    """

    def __init__(self,
                 settings: Settings,
                 endpoints_model_factory: IEndpointsFactory[Endpoints],
                 accept_language: Optional[enums.AcceptLanguage] = None,
                 ):
        """Initialize the main TASE client.
        
        Args:
            settings: API configuration including authentication credentials
            endpoints_model_factory: Factory for creating endpoint configurations
            accept_language: Preferred language for API responses (optional)
        """
        super().__init__(settings, endpoints_model_factory, accept_language)
        self.funds = Funds(self, self._do_request)
        self.indices_basic = IndicesBasic(self, self._do_request)
        self.indices_online = IndicesOnline(self, self._do_request)
        self.securities_basic = SecuritiesBasic(self, self._do_request)

    @staticmethod
    def _do_request(
            url: Tuple[Endpoints, EndpointGroup, Endpoint],
            params: parameters.BaseParameters,
            headers: head.Header,
            response_model: Type[T],
            resource: Optional[IResource] = NoResource(),
    ) -> T:
        """Execute HTTP request to TASE API endpoint.
        
        Args:
            url: Tuple containing base URL, endpoint group, and specific endpoint
            params: Request parameters to include in the API call
            headers: HTTP headers including authentication and language preferences
            response_model: Pydantic model class for response validation
            resource: Optional resource path extension for the URL
            
        Returns:
            Validated response object of the specified model type
            
        Raises:
            RuntimeError: If the request fails or is rejected by the API
        """
        _url = f"{url[0].base_url}/{url[1].group_url}/{url[2].url}{resource.resource_path}"
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
