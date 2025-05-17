from abc import ABC, abstractmethod
from requests_.urls import Endpoints, BaseModelGeneric
from typing import Generic


class IEndpointsFactory(ABC, Generic[BaseModelGeneric]):

    @abstractmethod
    def get_endpoints(self) -> Endpoints[BaseModelGeneric]:
        pass

