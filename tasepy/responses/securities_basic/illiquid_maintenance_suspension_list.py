from datetime import datetime
from pydantic import Field
from ..responses import ResponseComponent, Root


class IlliquidMaintenanceSuspensionItem(ResponseComponent):
    """Individual security illiquid maintenance and suspension information.
    
    Represents a security with its status classification and effective date
    for maintenance, suspension, and illiquidity tracking.
    """
    security_id: int = Field(alias="securityID")
    list_type_id: str
    status_date: datetime


class IlliquidMaintenanceSuspensionList(ResponseComponent):
    """Complete illiquid maintenance and suspension list response from TASE securities API.
    
    Contains securities that are on maintenance, suspension or illiquid lists
    for the next trading day on the Tel Aviv Stock Exchange.
    """
    illiquid_maintenance_and_suspension_list: Root[IlliquidMaintenanceSuspensionItem]
