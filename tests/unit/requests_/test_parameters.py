# from requests_.parameters import BaseParameters
# from enum import Enum
#
#
# class TestBaseParameters:
#
#     def test_aliasing(self):
#
#         class DemoChild(BaseParameters):
#             field_name: str
#
#         child = DemoChild(field_name='value')
#         assert child.model_dump() == {'fieldName': 'value'}
#
#     def test_enum_serialization(self):
#
#         class DemoEnum(Enum):
#             value = 'value string'
#
#         class DemoChild(BaseParameters):
#             field_name: DemoEnum
#
#         child = DemoChild(field_name=DemoEnum.value)
#         assert child.model_dump() == {'fieldName': 'value string'}
#
#     def test_null_arguments_for_fields_with_defaults(self):
#
#         class DemoChild(BaseParameters):
#             field_name: str = 'default value'
#
#         arguments = {'field_name': None}
#         child = DemoChild(**arguments)
#         assert child.model_dump() == {'fieldName': 'default value'}
#
#
# if __name__ == '__main__':
#     TestBaseParameters().test_aliasing()
#     TestBaseParameters().test_enum_serialization()
#     TestBaseParameters().test_null_arguments_for_fields_with_defaults()
