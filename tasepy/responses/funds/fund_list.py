from typing import Any, List, Optional
from ..responses import ResponseComponent


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
