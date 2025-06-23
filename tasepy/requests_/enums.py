from enum import Enum


class AcceptLanguage(Enum):
    """Language preference for API responses.
    
    Specifies the preferred language for API response content and descriptions.
    Used in request headers to control localization of returned data.
    """
    en = 'en-US'
    he = 'he-IL'


class ListingStatusId(str, Enum):
    """Fund listing status identifiers.
    
    Represents the current status of funds in the TASE system:
    - Active: Currently operating funds
    - Merged: Funds that have been merged with other funds
    - Liquidated: Funds that have been liquidated
    - Delisted: Funds that have been removed from listing
    """
    Active = '1'
    Merged = '2'
    Liquidated = '3'
    Delisted = '4'
