from typing import Any, Optional
from ..responses import ResponseComponent, CodeValuePair, Root


class ResultItem(ResponseComponent):
    fund_id: int
    fund_name: str
    fund_long_name: str
    listing_status_id: int
    classification_major: CodeValuePair
    classification_main: Optional[CodeValuePair]
    classification_secondary: Optional[CodeValuePair]
    exposure_profile: str
    isin: Optional[str]
    underlying_asset: Any
    fund_type: Any


class FundList(ResponseComponent):
    funds: Root[ResultItem]
