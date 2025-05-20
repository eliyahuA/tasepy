"""
    Manufacture am instance of pydentic model that contains the endpoints
"""
import pathlib
import typeguard

import yaml
import pathlib as p

from collections.abc import Mapping
from tasepy.requests_.urls import BaseModelGeneric
from tasepy.endpoints.factories.interfaces import IEndpointsFactory
from typing import Any, Dict, Type, Union


class YAMLFactory(IEndpointsFactory[BaseModelGeneric]):

    @typeguard.typechecked
    def __init__(self, yaml_path: Union[str, p.Path, Dict[str, Any]], endpoints_model: Type[BaseModelGeneric]):
        self.yaml = self._get_yaml(yaml_path) if not isinstance(yaml_path, Mapping) else yaml_path
        self.endpoints_model = endpoints_model

    def get_endpoints(self) -> BaseModelGeneric:
        return self.endpoints_model(**self.yaml)

    @staticmethod
    def _get_path(path: str) -> pathlib.Path:
        return p.Path(path)

    @classmethod
    def _get_yaml(cls, yaml_path: Union[str, p.Path]) -> Dict[str, Any]:
        yaml_path = cls._get_path(yaml_path) if isinstance(yaml_path, str) else yaml_path
        if not yaml_path.exists():
            raise FileNotFoundError(f"Endpoints configuration yaml was not found at {yaml_path}")
        with open(yaml_path, "r") as stream:
            return yaml.safe_load(stream)


if __name__ == '__main__':
    from models.endpoints import Endpoints

    yaml_factory = YAMLFactory('./endpoints/endpoints.yaml', Endpoints)
    endpoints = yaml_factory.get_endpoints()
    print(endpoints)
