from pydantic import BaseModel
from typing import Generic, TypeVar

BaseModelGeneric = TypeVar('BaseModelGeneric', bound=BaseModel)


class Endpoint(BaseModel):
    """Individual API endpoint URL configuration."""
    url: str


class EndpointGroup(BaseModel):
    """Base configuration for grouped API endpoints with shared URL prefix."""
    group_url: str


class Funds(EndpointGroup):
    """Fund-related API endpoint URL configurations.
    
    Contains URLs for fund listings, classifications, exposures, and various
    fund-specific data endpoints in the TASE DataWise API.
    """
    funds_list: Endpoint
    currencies_exposure_profile: Endpoint
    distribution_commission: Endpoint
    fund_types: Endpoint
    listing_status: Endpoint
    classification: Endpoint
    payment_policy: Endpoint
    shares_exposure_profile: Endpoint
    stock_exchange: Endpoint
    tax_status: Endpoint
    tracking_fund_classification: Endpoint
    underlying_assets: Endpoint


class BasicIndices(EndpointGroup):
    """Basic indices API endpoint URL configurations.
    
    Contains URLs for index listings and component data in the TASE DataWise API.
    """
    indices_list: Endpoint
    index_components_basic: Endpoint


class Securities(EndpointGroup):
    """Basic securities API endpoint URL configurations.
    
    Contains URLs for securities listings, companies, and trading data in the TASE DataWise API.
    """
    trade_securities_list: Endpoint
    delisted_securities_list: Endpoint
    companies_list: Endpoint
    illiquid_maintenance_suspension_list: Endpoint
    trading_code_list: Endpoint
    securities_types: Endpoint


class IndicesOnline(EndpointGroup):
    """Online indices API endpoint URL configurations.
    
    Contains URLs for real-time indices data including intraday rates, 
    last rates, and trading rate types in the TASE DataWise API.
    """
    intraday: Endpoint
    last_rate: Endpoint
    trading_rate_types: Endpoint


class Endpoints(BaseModel, Generic[BaseModelGeneric]):
    """Complete API endpoint configuration structure.
    
    Root configuration containing base URL and organized endpoint groups
    for API domains.
    """
    base_url: str
    funds: Funds
    indices: BasicIndices
    securities: Securities
    indices_online: IndicesOnline


if __name__ == "__main__":
    pass
