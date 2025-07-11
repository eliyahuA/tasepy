from typing import Optional
from ..responses import ResponseComponent, Root


class IntradayItem(ResponseComponent):
    """Individual intraday index data item."""
    date_time: str
    index_id: int
    last_index_rate: float
    change: Optional[float] = None
    last_sale_time: Optional[str] = None
    index_trading_rate_type_id: str


class IntraDay(ResponseComponent):
    """Intraday index trading data."""
    get_index_trading_data_intra_day: Root[IntradayItem]
