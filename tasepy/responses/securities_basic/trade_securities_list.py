from datetime import datetime
from typing import List
from ..responses import ResponseComponent, Root


class TradeSecurityItem(ResponseComponent):
    """Individual traded security information.
    
    Represents a security that was traded on a specific date with comprehensive
    identification details, sector classification, and index inclusion data.
    """
    trade_date: datetime
    security_id: int
    security_full_type_code: str
    isin: str
    corporate_id: str
    issuer_id: int
    security_is_included_in_continuous_indices: List[int]
    security_name: str
    symbol: str
    company_super_sector: str
    company_sector: str
    company_sub_sector: str
    company_name: str


class TradeSecuritiesList(ResponseComponent):
    """Complete trade securities list response from TASE securities API.
    
    Contains extensive current and historical data for securities traded
    on the Tel Aviv Stock Exchange for a specific trading date.
    """
    trade_securities_list: Root[TradeSecurityItem]