from pydantic import Field
from ..responses import ResponseComponent, Root


class TradingRateTypeItem(ResponseComponent):
    """Individual trading rate type classification item."""
    index_trading_rate_type_id: str = Field(alias="indexTradingRateTypeId")
    index_trading_rate_type_desc: str = Field(alias="indexTradingRateTypeDesc")


class TradingRateTypes(ResponseComponent):
    """Trading rate types classification data for indices."""
    get_index_trading_rate_types: Root[TradingRateTypeItem] = Field(alias="getIndexTradingRateTypes")