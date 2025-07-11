from pydantic import Field
from typing import List, Union
from ..responses import ResponseComponent


class LastRateItem(ResponseComponent):
    """Individual last rate index data item."""
    index_id: int = Field(alias="indexId")
    last_index_rate: float = Field(alias="lastIndexRate")
    change: float
    last_sale_time: str = Field(alias="lastSaleTime")
    index_trading_rate_type_id: str = Field(alias="indexTradingRateTypeId")


class LastRate(ResponseComponent):
    """Last rate index trading data.
    
    Can contain either a single item (when filtering by index_id) 
    or a list of items (when retrieving all indices).
    """
    get_index_trading_data_intra_day: Union[LastRateItem, List[LastRateItem]] = Field(alias="getIndexTradingDataIntraDay")