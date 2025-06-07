from typing import Protocol, Tuple, Type, TypeVar, Optional
from tasepy.requests_.urls import Endpoints, EndpointGroup, Endpoint
from tasepy.requests_.parameters import BaseParameters
from tasepy.requests_.headers import Header
from tasepy.requests_.resources import IResource

T = TypeVar('T')


class APIRequestExecutor(Protocol):
    def __call__(
        self,
        *,  # Force keyword-only arguments
        url: Tuple[Endpoints, EndpointGroup, Endpoint],
        params: BaseParameters,
        headers: Header,
        response_model: Type[T],
        resource: Optional[IResource] = None,
    ) -> T: ...
