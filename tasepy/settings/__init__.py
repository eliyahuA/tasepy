"""Configuration management for TASE DataWise API.

Provides settings models and builder pattern for flexible API client
configuration including authentication and connection parameters.
"""
from .settings import Settings, ApiKeyFile
from .builder import SettingsBuilder
