from enum import Enum


class AcceptLanguage(Enum):
    en = 'en-US'
    he = 'he-IL'


class ListingStatusId(str, Enum):
    _1 = '1'
    _2 = '2'
    _3 = '3'
    _4 = '4'
