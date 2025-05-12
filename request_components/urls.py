from pydantic import BaseModel
from typing import Generic, TypeVar

BaseModelGeneric = TypeVar('BaseModelGeneric', bound=BaseModel)


class Endpoint(BaseModel):
    url: str


class EndpointGroup(BaseModel):
    group_url: str


class Funds(EndpointGroup):
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

    indices_list: Endpoint
    index_components_basic: Endpoint


class Endpoints(BaseModel, Generic[BaseModelGeneric]):
    base_url: str
    funds: Funds
    indices: BasicIndices


if __name__ == "__main__":
    pass
