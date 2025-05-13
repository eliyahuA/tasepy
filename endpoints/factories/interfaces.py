from abc import ABC, abstractmethod
from request_components.urls import Endpoints, BaseModelGeneric
from typing import Generic


class IEndpointsFactory(ABC, Generic[BaseModelGeneric]):

    @abstractmethod
    def get_endpoints(self) -> Endpoints[BaseModelGeneric]:
        pass

