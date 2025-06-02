from typing import List, Optional
from ..responses import ResponseComponent


class SecondaryItem(ResponseComponent):
    code: int
    value: str


class MainItem(ResponseComponent):
    code: int
    value: str
    classification_secondary: Optional[List[SecondaryItem]] = None


class ClassificationItem(ResponseComponent):
    classification_major_id: int
    classification_major_value: str
    classification_main: Optional[List[MainItem]] = None


class Root(ResponseComponent):
    result: List[ClassificationItem]
    total: int


class MutualFundClassification(ResponseComponent):
    fund_classification: Root
