"""TASE DataWise API Python SDK.

A comprehensive Python SDK for accessing the Tel Aviv Stock Exchange (TASE) 
DataWise API. Provides typed clients, request builders, and response models
for funds and indices data.

Modules:
    clients: API client implementations (tailored and OpenAPI-generated)

    settings: Configuration management with flexible authentication

    requests_: Request building components (headers, parameters, URLs, enums)

    responses: Pydantic models for parsing and validating API responses

    endpoints: YAML-based endpoint configuration and factory patterns

Example:
    >>> from tasepy.settings import SettingsBuilder
    >>> from tasepy.clients.tailored import Client
    >>> from tasepy.endpoints.factories.yaml_factory import YAMLFactory
    >>> from tasepy.requests_.urls import Endpoints
    >>> 
    >>> client = Client(
    ...     SettingsBuilder().with_apikey(environment="TASE_API_KEY").build(),
    ...     YAMLFactory('./endpoints.yaml', Endpoints)
    ... )
    >>> funds = client.funds.get_list()
"""
from . import clients
from . import endpoints
from . import requests_
from . import responses
from . import settings
