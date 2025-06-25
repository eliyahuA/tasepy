from pathlib import Path
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel
from typing import TypeVar, List, Generic


class ResponseComponent(BaseModel):
    """Base model for TASE API response parsing.
    
    Provides consistent field naming (camelCase conversion), validation,
    and serialization behavior for all API response models.
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
        extra='forbid'
    )


class CodeValuePair(ResponseComponent):
    """Standard code-value pair structure.
    
    Common pattern across TASE API responses for classifications
    and categorical data with numeric codes and text descriptions.
    """
    code: int
    value: str


T = TypeVar('T', bound=ResponseComponent)


class Root(ResponseComponent, Generic[T]):
    """Standard API response wrapper.
    
    Wraps result arrays with total count metadata following
    consistent TASE API response structure pattern.
    """
    result: List[T]
    total: int


class ForgivingResponse(ResponseComponent):
    """Unvalidated response model for development and debugging.
    
    Bypasses Pydantic validation to handle unknown or changing API structures.
    Should be avoided in production code - use typed response models instead.
    """
    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,
        arbitrary_types_allowed=True
    )

    def save_pretty_json(self, target_file_path: Path) -> None:
        with open(target_file_path, 'w', encoding='utf-8') as f:
            f.write(self.model_dump_json(indent=4))
