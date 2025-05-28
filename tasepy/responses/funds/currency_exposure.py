from typing import List
from ..responses import ResponseComponent


class ExposureItem(ResponseComponent):
    code: str
    value: str


class CurrencyExposure(ResponseComponent):
    result: List[ExposureItem]
    total: int
