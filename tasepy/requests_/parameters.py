from pydantic import BaseModel, Field, ConfigDict, model_validator
from pydantic.alias_generators import to_camel

from . import enums


class BaseParameters(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
    )

    @model_validator(mode='before')
    @classmethod
    def remove_none_values(cls, data):
        """
        Remove Arguments with None values before instantiating
        """
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return data

    def model_dump(self, *args, **kwargs):
        """
        Set Default dumping mode to json
        """
        kwargs['mode'] = 'json'
        return super().model_dump(*args, **kwargs)


class FundList(BaseParameters):

    listing_status_id: enums.ListingStatusId = Field(
        default=enums.ListingStatusId._1
    )
