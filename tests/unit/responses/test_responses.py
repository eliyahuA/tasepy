import re
from tasepy.responses import ForgivingResponse
from pytest import fixture


class TestForgivingResponse:
    @fixture
    def dummy_json(self) -> str:
        return """
            {
                "root": {
                    "children": [
                        {
                            "numeric value": 1,
                            "string value": "hello world"
                        },
                        {
                            "numeric value": 2,
                            "string value": "שלום עולם!"
                        }
                    ],
                    "total": 2
                }
            }      
        """

    @fixture
    def dummy_response(self, dummy_json) -> ForgivingResponse:
        return ForgivingResponse.model_validate_json(dummy_json)

    def test_creation(self, dummy_response):
        assert str(dummy_response) == ("root={'children': [{'numeric value': 1, 'string value': 'hello world'}, "
                                       "{'numeric value': 2, 'string value': 'שלום עולם!'}], 'total': 2}")

    def test_export(self, dummy_json, dummy_response, tmp_path):
        json_path = tmp_path / 'dummy.json'
        dummy_response.save_pretty_json(json_path)
        with open(json_path, 'r', encoding='utf-8') as f:
            file_contents = f.read()
        # ignore indentation while comparing
        assert (re.sub(r'[ \t]+', '', file_contents.strip()) ==
                re.sub(r'[ \t]+', '', dummy_json.strip()))

