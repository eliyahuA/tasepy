from pathlib import Path
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from typing import TypeVar, List, Generic


class ResponseComponent(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
        extra='forbid'
    )


class CodeValuePair(ResponseComponent):
    code: int
    value: str


T = TypeVar('T', bound=ResponseComponent)


class Root(ResponseComponent, Generic[T]):
    result: List[T]
    total: int


class ForgivingResponse(ResponseComponent):
    """
        Use if no validation is to be performed on TASE API responses.
        Should be avoided unless for development purposes.
    """
    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,
        arbitrary_types_allowed=True
    )

    def save_pretty_json(self, target_file_path: Path) -> None:
        with open(target_file_path, 'w', encoding='utf-8') as f:
            f.write(self.model_dump_json(indent=4))
