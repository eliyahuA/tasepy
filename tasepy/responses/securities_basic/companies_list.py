from typing import Optional
from ..responses import ResponseComponent, Root


class CompanyItem(ResponseComponent):
    """Individual company information in the securities companies list.
    
    Represents a single company listed on TASE with identification details,
    sector classification, and dual listing status.
    """
    company_name: str
    tase_sector: str
    company_full_name: str
    issuer_id: int
    corporate_id: str
    is_dual: bool


class CompaniesList(ResponseComponent):
    """Complete companies list response from TASE securities API.
    
    Contains the full list of companies listed on the Tel Aviv Stock Exchange
    with their basic identification and classification information.
    """
    companies_list: Root[CompanyItem]
