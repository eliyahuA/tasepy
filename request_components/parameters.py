import request_components.enums as enums
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class BaseParameters(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
    )

    def __init__(self, **kwargs):
        """
        Remove Arguments with None values before instantiating
        """
        kwargs = dict(filter(lambda item: item[1] is not None, kwargs.items()))
        super().__init__(**kwargs)

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


if __name__ == "__main__":
    kwargs = {'listing_status_id': None}
    m = FundList(**kwargs)
    # m = FundList(listing_status_id=enums.ListingStatusId._2)
    print(m)
    print(m.model_dump())
