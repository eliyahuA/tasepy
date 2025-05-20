from tasepy.endpoints.factories.yaml_factory import YAMLFactory
from tasepy.endpoints.factories.interfaces import IEndpointsFactory
from models.endpoints import Endpoints


def default_factory() -> IEndpointsFactory:
    return YAMLFactory('./endpoints/endpoints.yaml', Endpoints)
