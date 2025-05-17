from typing import Any, List, Optional
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from request_components.headers import FundList


class ResponseComponent(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
        extra='forbid'
    )


class Classification(ResponseComponent):
    code: int
    value: str


class ResultItem(ResponseComponent):
    fund_id: int
    fund_name: str
    fund_long_name: str
    listing_status_id: int
    classification_major: Classification
    classification_main: Classification
    classification_secondary: Optional[Classification]
    exposure_profile: str
    isin: str
    underlying_asset: Any
    fund_type: Any


class Funds(ResponseComponent):
    result: List[ResultItem]
    total: int


class FundList(ResponseComponent):
    funds: Funds


if __name__ == "__main__":
    # funds = FundList(
    #     funds=FundList.Funds(
    #         result=[FundList.ResultItem()],
    #         total=100
    #     ),
    # )

    string_json = """
    {
    "funds": {
        "result": [
            {
                "fundId": 1142538,
                "isin": "IL0011425381",
                "fundName": "IBITEC   FUND",
                "fundLongName": "I.B.I. (5D) Tech Fund \u2013 High Technology",
                "listingStatusId": 1,
                "exposureProfile": "5D",
                "underlyingAsset": [
                    {
                        "code": 438,
                        "weight": 100,
                        "value": "TA Tech - Elite"
                    }
                ],
                "classificationMajor": {
                    "code": 147,
                    "value": "Closed Fund"
                },
                "classificationMain": {
                    "code": 148,
                    "value": "Hitech Fund"
                },
                "classificationSecondary": null,
                "fundType": [
                    {
                        "code": 3,
                        "value": "Elite Tech - Closed fund"
                    }
                ]
            }
        ],
        "total": 1
        }
    }
    """

    f = FundList.model_validate_json(string_json)
    print(f)
