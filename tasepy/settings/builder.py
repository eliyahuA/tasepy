import os
import pathlib
import yaml

from typing import Optional, Callable
from tasepy.settings import Settings, ApiKeyFile
import typeguard


class SettingsBuilder:

    def __init__(self):
        self._api_key: Optional[str] = None
        self._api_key_provider: Optional[Callable[[], str]] = None

    @typeguard.typechecked
    def with_apikey(self,
                    key: Optional[str] = None,
                    environment: Optional[str] = None,
                    file_path: Optional[str] = None,
                    key_provider: Optional[Callable[[], str]] = None,
                    ) -> 'SettingsBuilder':
        """Set the API key using one of multiple methods.
        By default, if no args passed key will be loaded from environment variable of name TASE_API_KEY
        Args:
            key: Direct API key value
            environment: name environment variable to load the key from
            file_path: path to file load the key from
            key_provider: Callable function that returns an API key

        Returns:
            Self for method chaining
        """
        if key is not None:
            self._api_key = key
        elif environment:
            self._api_key = os.environ.get(environment)
        elif file_path:
            path = pathlib.Path(file_path)
            if path.suffix != '.yaml':
                raise TypeError('The file must be a YAML file.')
            if not path.exists():
                raise FileNotFoundError(f'File not found at {path.absolute()}')
            with open(file_path, 'r') as f:
                key_yaml = yaml.safe_load(f)
                self._api_key = ApiKeyFile(**key_yaml).key
        elif key_provider is not None:
            self._api_key_provider = key_provider

        return self

    @typeguard.typechecked
    def build(self) -> Settings:
        """Build and return a Settings instance."""
        api_key = self._api_key

        # Use provider if direct key not set
        if api_key is None and self._api_key_provider is not None:
            api_key = self._api_key_provider()

        if api_key is None:
            raise ValueError("API key must be provided")

        return Settings(api_key=api_key)
