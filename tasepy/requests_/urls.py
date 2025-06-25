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


class Endpoints(BaseModel, Generic[BaseModelGeneric]):
    """Complete API endpoint configuration structure.
    
    Root configuration containing base URL and organized endpoint groups
    for funds and indices domains.
    """
    base_url: str
    funds: Funds
    indices: BasicIndices


if __name__ == "__main__":
    pass
