import request_components.enums as enums
from pydantic import BaseModel, Field
from typing import Dict


class FundList(BaseModel):

    listing_status_id: enums.ListingStatusId = Field(
        default=enums.ListingStatusId._1,
        serialization_alias='listingStatusId'
    )


if __name__ == "__main__":
    m = FundList()
    print(m.model_dump(by_alias=True))
    print(m.model_dump_json(by_alias=True))
    print(m.model_dump_json(by_alias=True))
