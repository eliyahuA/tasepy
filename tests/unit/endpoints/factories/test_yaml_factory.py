import pytest
import yaml
from tasepy.endpoints.factories import YAMLFactory
from tasepy.requests_.urls import BaseModelGeneric
from typing import Generic, Type, Dict, Any, Generator
from pydantic import BaseModel
from pathlib import Path


class DummyModel(BaseModel, Generic[BaseModelGeneric]):
    field: str


@pytest.fixture
def pydantic_model() -> Type[BaseModelGeneric]:
    return DummyModel


@pytest.fixture
def dummy_dict() -> Dict[str, Any]:
    return {'field': 'value'}


@pytest.fixture
def dummy_yaml_file(tmp_path, dummy_dict) -> Generator[Path]:
    yaml_file_path = tmp_path / 'dummy.yaml'
    with open(yaml_file_path, 'w') as f:
        yaml.dump(dummy_dict, f)
    yield yaml_file_path


@pytest.fixture
def dummy_yaml_file_str_path(dummy_yaml_file):
    return str(dummy_yaml_file)


class TestYAMLFactory:

    @pytest.mark.parametrize(
        "dummy_dict,pydantic_model",
        [
            (dummy_dict, pydantic_model),
            (dummy_yaml_file, pydantic_model),
            (dummy_yaml_file_str_path, pydantic_model)
        ],
        indirect=True
    )
    def test_get_endpoints(self, dummy_dict, pydantic_model):
        yaml_factory = YAMLFactory(dummy_dict, pydantic_model)
        loaded_model = yaml_factory.get_endpoints()
        assert isinstance(loaded_model, DummyModel)
        assert 'field' in loaded_model.model_fields.keys()
        assert loaded_model.field == 'value'
