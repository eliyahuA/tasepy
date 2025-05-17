from typing import Any, List, Optional
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ResponseComponent(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
        extra='forbid'
    )



