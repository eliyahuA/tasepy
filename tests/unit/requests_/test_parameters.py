from tasepy.requests_.parameters import BaseParameters, FundList
from enum import Enum


class TestBaseParameters:

    def test_aliasing(self):

        class DemoChild(BaseParameters):
            field_name: str

        child = DemoChild(field_name='value')
        assert child.model_dump() == {'fieldName': 'value'}

    def test_enum_serialization(self):

        class DemoEnum(Enum):
            value = 'value string'

        class DemoChild(BaseParameters):
            field_name: DemoEnum

        child = DemoChild(field_name=DemoEnum.value)
        assert child.model_dump() == {'fieldName': 'value string'}

    def test_null_arguments_for_fields_with_defaults(self):

        class DemoChild(BaseParameters):
            field_name: str = 'default value'

        arguments = {'field_name': None}
        child = DemoChild(**arguments)
        assert child.model_dump() == {'fieldName': 'default value'}


class TestFundListParameters:

    def test_default(self):
        f = FundList()
        assert f.model_dump() == {'listingStatusId': '1'}
