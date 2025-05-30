from typing import Callable, Tuple, Type, TypeVar
from tasepy.requests_.urls import Endpoints, EndpointGroup, Endpoint
from tasepy.requests_.parameters import BaseParameters
from tasepy.requests_.headers import Header

T = TypeVar('T')

RequestCallable = Callable[
    [
        Tuple[Endpoints, EndpointGroup, Endpoint],
        BaseParameters,
        Header,
        Type[T]
    ],
    T
]
