from typing import List
from ..responses import ResponseComponent


class ExposureItem(ResponseComponent):
    code: str
    value: str


class Root(ResponseComponent):
    result: List[ExposureItem]
    total: int


class CurrencyExposure(ResponseComponent):
    currency_exposure_profile: Root
