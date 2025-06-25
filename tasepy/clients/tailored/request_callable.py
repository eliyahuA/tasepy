from typing import Protocol, Tuple, Type, TypeVar, Optional
from tasepy.requests_.urls import Endpoints, EndpointGroup, Endpoint
from tasepy.requests_.parameters import BaseParameters
from tasepy.requests_.headers import Header
from tasepy.requests_.resources import IResource

T = TypeVar('T')


class APIRequestExecutor(Protocol):
    """Protocol defining the interface for API request execution.
    
    This protocol ensures consistent request handling across different
    client implementations by defining the required method signature
    for executing API requests.
    """
    def __call__(
        self,
        *,  # Force keyword-only arguments
        url: Tuple[Endpoints, EndpointGroup, Endpoint],
        params: BaseParameters,
        headers: Header,
        response_model: Type[T],
        resource: Optional[IResource] = None,
    ) -> T:
        """Execute an API request.
        
        Args:
            url: Tuple containing base URL, endpoint group, and specific endpoint
            params: Request parameters to include in the API call
            headers: HTTP headers including authentication and language preferences
            response_model: Pydantic model class for response validation
            resource: Optional resource path extension for the URL
            
        Returns:
            Validated response object of the specified model type
        """
        ...
