from typing import Optional
from ..responses import ResponseComponent, Root


class SecurityItem(ResponseComponent):
    security_id: int
    isin: Optional[str] = None
    symbol: str
    security_name: str


class IndexComponents(ResponseComponent):
    index_components: Root[SecurityItem]
