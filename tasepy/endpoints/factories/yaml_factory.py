import pathlib
import typeguard

import yaml
import pathlib as p

from collections.abc import Mapping
from tasepy.requests_.urls import BaseModelGeneric
from typing import Any, Dict, Type, Union

from .interfaces import IEndpointsFactory


class YAMLFactory(IEndpointsFactory[BaseModelGeneric]):
    """Factory for creating Pydantic endpoint models from YAML configuration.
    
    This factory reads endpoint configuration from YAML files or dictionaries
    and creates instances of the specified Pydantic model type. It supports
    both file paths and pre-loaded configuration dictionaries.
    
    Type Parameters:
        BaseModelGeneric: The Pydantic model type to be instantiated
    
    Attributes:
        yaml: The loaded YAML configuration data as a dictionary
        endpoints_model: The Pydantic model class to instantiate
    """

    @typeguard.typechecked
    def __init__(self, yaml: Union[str, p.Path, Dict[str, Any]], endpoints_model: Type[BaseModelGeneric]):
        """Initialize the YAML factory with configuration source and model type.
        
        Args:
            yaml: Path to YAML file (string or Path object) or pre-loaded configuration dictionary
            endpoints_model: The Pydantic model class to instantiate from the YAML data
            
        Raises:
            FileNotFoundError: If yaml_path is a file path that doesn't exist
        """
        self.yaml = self._get_yaml(yaml) if not isinstance(yaml, Mapping) else yaml
        self.endpoints_model = endpoints_model

    def get_endpoints(self) -> BaseModelGeneric:
        """Create and return an endpoint configuration object from YAML data.
        
        Returns:
            An instance of the configured Pydantic model populated with YAML data
        """
        return self.endpoints_model(**self.yaml)

    @staticmethod
    def _get_path(path: str) -> pathlib.Path:
        """Convert string path to Path object.
        
        Args:
            path: String representation of file path
            
        Returns:
            Path object for the given string path
        """
        return p.Path(path)

    @classmethod
    def _get_yaml(cls, yaml_path: Union[str, p.Path]) -> Dict[str, Any]:
        """Load and parse YAML configuration from file.
        
        Args:
            yaml_path: Path to the YAML configuration file (string or Path object)
            
        Returns:
            Dictionary containing the parsed YAML configuration data
            
        Raises:
            FileNotFoundError: If the specified YAML file does not exist
        """
        yaml_path = cls._get_path(yaml_path) if isinstance(yaml_path, str) else yaml_path
        if not yaml_path.exists():
            raise FileNotFoundError(f"Endpoints configuration yaml was not found at {yaml_path}")
        with open(yaml_path, "r") as stream:
            return yaml.safe_load(stream)
