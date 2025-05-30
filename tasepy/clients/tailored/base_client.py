from typing import Optional

from tasepy.endpoints.factories.interfaces import IEndpointsFactory
from tasepy.requests_ import enums
from tasepy.requests_.urls import Endpoints
from tasepy.settings import Settings


class BaseClient:

    def __init__(self,
                 settings: Settings,
                 endpoints_model_factory: IEndpointsFactory[Endpoints],
                 accept_language: Optional[enums.AcceptLanguage] = None,
                 ):
        self.settings = settings
        self.endpoints = endpoints_model_factory.get_endpoints()
        self.accept_language = accept_language
