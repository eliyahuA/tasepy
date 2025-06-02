from ..responses import ResponseComponent, Root


class ExposureItem(ResponseComponent):
    code: str
    value: str


class CurrencyExposure(ResponseComponent):
    currency_exposure_profile: Root[ExposureItem]
