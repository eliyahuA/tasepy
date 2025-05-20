from typing import Any, List, Optional
from tasepy.responses.responses import ResponseComponent


class Classification(ResponseComponent):
    code: int
    value: str


class ResultItem(ResponseComponent):
    fund_id: int
    fund_name: str
    fund_long_name: str
    listing_status_id: int
    classification_major: Classification
    classification_main: Optional[Classification]
    classification_secondary: Optional[Classification]
    exposure_profile: str
    isin: Optional[str]
    underlying_asset: Any
    fund_type: Any


class Funds(ResponseComponent):
    result: List[ResultItem]
    total: int


class FundList(ResponseComponent):
    funds: Funds


if __name__ == "__main__":

    import json
    with open('./responses/fund-list.json', 'r') as f:
        data = json.load(f)
    f = FundList.model_validate(data)

    print(f)
    print(f.funds.result[0].fund_id)
