from ..responses import ResponseComponent, Root


class TradingCodeItem(ResponseComponent):
    """Individual trading code classification information.
    
    Represents a trading list type with ID and Hebrew description
    for securities maintenance, suspension, and liquidity classification.
    """
    list_type_id: int
    list_type_desc: str


class TradingCodeList(ResponseComponent):
    """Complete trading code list response from TASE securities API.
    
    Contains the classification system for trading list types used
    on the Tel Aviv Stock Exchange for maintenance and trading status.
    """
    trading_list_code: Root[TradingCodeItem]
