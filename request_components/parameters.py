import request_components.enums as enums
from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class BaseParameters(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
    )

    def model_dump(self, *args, **kwargs):
        kwargs['mode'] = 'json'
        return super().model_dump(*args, **kwargs)


class FundList(BaseParameters):

    listing_status_id: enums.ListingStatusId2 = Field(
        default=enums.ListingStatusId2.one
    )


if __name__ == "__main__":
    kwargs = {'listing_status_id': enums.ListingStatusId._2}
    # m = FundList(**kwargs)
    m = FundList(listing_status_id=enums.ListingStatusId2.two)
    print(m)
    print(m.model_dump())
