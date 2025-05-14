import request_components.enums as enums

from pydantic import BaseModel, field_serializer, Field, ConfigDict, model_validator, model_serializer
from typing import Any, Dict


class Header(BaseModel):

    model_config = ConfigDict(
        alias_generator=lambda field_name: field_name.replace("_", "-"),
        populate_by_name=True,
        serialize_by_alias=True,
    )

    accept: str = "application/json"
    apikey: str

    @model_validator(mode='before')
    @classmethod
    def remove_none_values(cls, data):
        """
        Remove Arguments with None values before instantiating
        """
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return data

    def model_dump(self, *args, mask: bool = False, **kwargs):
        """
        Set Default dumping mode to json
        Add option to mask sensitive fields
        """
        kwargs['mode'] = 'json'
        data = super().model_dump(*args, **kwargs)
        if mask:
            data['apikey'] = "*"*len(data['apikey'])
        return data


class FundList(Header):

    accept_language: enums.AcceptLanguage = enums.AcceptLanguage.he


if __name__ == "__main__":
    h = FundList(apikey="sdfmsidfh823", accept_language=None)
    print(h.model_dump())
    print(h.model_dump(mask=True))
