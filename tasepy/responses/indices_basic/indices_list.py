from ..responses import ResponseComponent, Root
from typing import Optional


class IndexItem(ResponseComponent):
    index_id: int
    index_name: str
    isin: Optional[str] = None


class IndicesList(ResponseComponent):
    indices_list: Root[IndexItem]
