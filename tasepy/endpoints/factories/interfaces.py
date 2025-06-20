from abc import ABC, abstractmethod
from tasepy.requests_.urls import BaseModelGeneric
from typing import Generic


class IEndpointsFactory(ABC, Generic[BaseModelGeneric]):
    """Abstract factory interface for creating endpoint configuration objects.
    
    This interface defines the contract for factories that create Pydantic model
    instances containing endpoint configuration data. The generic type parameter
    allows for different types of endpoint models to be created.
    
    Type Parameters:
        BaseModelGeneric: The Pydantic model type to be created by the factory
    """

    @abstractmethod
    def get_endpoints(self) -> BaseModelGeneric:
        """Create and return an endpoint configuration object.
        
        Returns:
            An instance of the configured Pydantic model containing endpoint data
        """
        pass

