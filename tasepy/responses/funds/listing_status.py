from typing import List
from ..responses import ResponseComponent


class Item(ResponseComponent):
    listing_status_id: int
    listing_status_desc: str


class Root(ResponseComponent):
    result: List[Item]


class ListingStatus(ResponseComponent):
    listing_status: Root
