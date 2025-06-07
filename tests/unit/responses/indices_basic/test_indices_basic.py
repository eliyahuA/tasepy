from tasepy.responses import indices_basic
from ..common import custom_open
from functools import partial

custom_open = partial(custom_open, caller_path_string=__file__)


def test_indices_list():
    with custom_open(json_name="indices-list") as f:
        sample_json = f.read()
    model_instance = indices_basic.IndicesList.model_validate_json(sample_json)
    assert model_instance is not None
    assert isinstance(model_instance, indices_basic.IndicesList)


def test_components():
    with custom_open(json_name="components") as f:
        sample_json = f.read()
        model_instance = indices_basic.IndexComponents.model_validate_json(sample_json)
        assert model_instance is not None
        assert isinstance(model_instance, indices_basic.IndexComponents)
