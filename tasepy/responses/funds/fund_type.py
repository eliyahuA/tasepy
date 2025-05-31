from typing import List
from ..responses import ResponseComponent


class Item(ResponseComponent):
    code: int
    value: str


class Root(ResponseComponent):
    result: List[Item]
    total: int


class FundType(ResponseComponent):
    fund_type: Root
