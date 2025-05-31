from pathlib import Path
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
    """
        Use if no validation is to be performed on TASE API responses.
        Should be avoided unless for development purposes.
    """
    model_config = ConfigDict(
        extra='allow',
        validate_assignment=False,
        arbitrary_types_allowed=True
    )

    def save_pretty_json(self, target_file: Path) -> None:
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(self.model_dump_json(indent=4))
