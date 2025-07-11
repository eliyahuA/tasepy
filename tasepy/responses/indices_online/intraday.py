from pydantic import Field
from typing import Optional
from ..responses import ResponseComponent, Root


class IntradayItem(ResponseComponent):
    """Individual intraday index data item."""
    date_time: str = Field(alias="dateTime")
    index_id: int = Field(alias="indexId")
    last_index_rate: float = Field(alias="lastIndexRate")
    change: Optional[float] = None
    last_sale_time: Optional[str] = Field(alias="lastSaleTime", default=None)
    index_trading_rate_type_id: str = Field(alias="indexTradingRateTypeId")


class IntraDay(ResponseComponent):
    """Intraday index trading data."""
    get_index_trading_data_intra_day: Root[IntradayItem] = Field(alias="getIndexTradingDataIntraDay")