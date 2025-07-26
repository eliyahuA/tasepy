from typing import Optional

from tasepy.endpoints.factories.interfaces import IEndpointsFactory
from tasepy.requests_ import enums
from tasepy.requests_.urls import Endpoints
from tasepy.settings import Settings


class BaseClient:
    """Base client for TASE DataWise API.
    
    Provides common functionality and initialization for specialized clients.
    Contains shared settings, endpoints configuration, and default language preferences.
    """

    def __init__(self,
                 settings: Settings,
                 endpoints_model_factory: IEndpointsFactory[Endpoints],
                 accept_language: Optional[enums.AcceptLanguage] = None,
                 ):
        """Initialize the base client.
        
        Args:
            settings: API configuration including authentication credentials
            endpoints_model_factory: Factory for getting endpoint configurations
            accept_language: Preferred language for API responses (optional)
        """
        self.settings = settings
        self.endpoints = endpoints_model_factory.get_endpoints()
        self.accept_language = accept_language


class SpecializedClient(BaseClient):
    """Specialized client extending BaseClient functionality.
    
    This class serves as a template for domain-specific client implementations
    that require additional functionality beyond the base client capabilities.
    """
    pass
