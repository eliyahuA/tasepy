"""TASE DataWise API Python SDK.

A comprehensive Python SDK for accessing the Tel Aviv Stock Exchange (TASE) 
DataWise API. Provides typed clients, request builders, and response models
for funds and indices data.

Quick Start:
    >>> import tasepy
    >>> client = tasepy.quick_client()
    >>> funds = client.funds.get_list()
    >>> indices = client.indices_basic.get_list()

Advanced Usage:
    >>> from tasepy.settings import SettingsBuilder
    >>> from tasepy.client import Client
    >>> from tasepy.endpoints.factories.yaml_factory import YAMLFactory
    >>> from tasepy.requests_.urls import Endpoints
    >>> 
    >>> client = Client(
    ...     SettingsBuilder().with_apikey(environment="API_KEY").build(),
    ...     YAMLFactory(Endpoints, './endpoints.yaml')
    ... )
    >>> funds = client.funds.get_list()

Modules:
    client: API client implementation

    settings: Configuration management with flexible authentication

    requests_: Request building components (headers, parameters, URLs, enums)

    responses: Pydantic models for parsing and validating API responses

    endpoints: YAML-based endpoint configuration and factory patterns
"""
from . import client
from . import endpoints
from . import requests_
from . import responses
from . import settings

from typing import Optional


def quick_client(
        settings_instance: Optional[settings.Settings] = None,
        factory: Optional[endpoints.factories.interfaces.IEndpointsFactory] = None
) -> client.Client:
    """Create a tailored TASE API client with sensible defaults.
    
    Convenience function that eliminates the need to manually construct 
    SettingsBuilder and YAMLFactory objects for basic usage scenarios.
    
    Args:
        settings_instance: Custom settings instance. If None, creates default 
            settings with API key from environment variable.
        factory: Custom endpoints factory. If None, creates default YAML factory.
    
    Returns:
        Client: Configured client ready for API calls.
    """
    return client.Client(
        settings.SettingsBuilder().with_apikey().build() if settings_instance is None else settings_instance,
        endpoints.factories.YAMLFactory(requests_.urls.Endpoints) if factory is None else factory,
    )
