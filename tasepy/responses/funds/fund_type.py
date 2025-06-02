from typing import List
from ..responses import ResponseComponent, Root, CodeValuePair


class FundType(ResponseComponent):
    fund_type: Root[CodeValuePair]
