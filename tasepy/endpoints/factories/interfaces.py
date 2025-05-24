from abc import ABC, abstractmethod
from tasepy.requests_.urls import Endpoints, BaseModelGeneric
from typing import Generic


class IEndpointsFactory(ABC, Generic[BaseModelGeneric]):

    @abstractmethod
    def get_endpoints(self) -> BaseModelGeneric:
        pass

