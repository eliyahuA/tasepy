from enum import Enum


class AcceptLanguage(Enum):
    en = 'en-US'
    he = 'he-IL'


class ListingStatusId(str, Enum):
    Active = '1'
    Merged = '2'
    Liquidated = '3'
    Delisted = '4'
