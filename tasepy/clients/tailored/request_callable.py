from typing import Protocol, Tuple, Type, TypeVar
from tasepy.requests_.urls import Endpoints, EndpointGroup, Endpoint
from tasepy.requests_.parameters import BaseParameters
from tasepy.requests_.headers import Header

T = TypeVar('T')


class APIRequestExecutor(Protocol):
    def __call__(
        self,
        *,  # Force keyword-only arguments
        url: Tuple[Endpoints, EndpointGroup, Endpoint],
        params: BaseParameters,
        headers: Header,
        response_model: Type[T]
    ) -> T: ...
