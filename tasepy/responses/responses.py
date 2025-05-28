from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ResponseComponent(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
        extra='forbid'
    )


class ForgivingResponse(ResponseComponent):
    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,
        arbitrary_types_allowed=True
    )


if __name__ == '__main__':
    pass