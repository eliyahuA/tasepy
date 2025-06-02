from typing import List, Optional
from ..responses import ResponseComponent, CodeValuePair, Root


class MainItem(CodeValuePair):
    classification_secondary: Optional[List[CodeValuePair]] = None


class ClassificationItem(ResponseComponent):
    classification_major_id: int
    classification_major_value: str
    classification_main: Optional[List[MainItem]] = None


class MutualFundClassification(ResponseComponent):
    fund_classification: Root[ClassificationItem]
