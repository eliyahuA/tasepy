from datetime import datetime
from ..responses import ResponseComponent, Root


class DelistedSecurityItem(ResponseComponent):
    """Individual delisted security information.
    
    Represents a security that has been delisted with its final trading date,
    identification details, and trading symbol.
    """
    date_last_trade: datetime
    security_id: int
    security_name: str
    symbol: str


class DelistedSecuritiesList(ResponseComponent):
    """Complete delisted securities list response from TASE securities API.
    
    Contains securities that have been delisted from the Tel Aviv Stock Exchange
    during the specified period with their final trading information.
    """
    delisted_securities_list: Root[DelistedSecurityItem]
