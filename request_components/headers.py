from pydantic import BaseModel
import request_components.enums as enums


class Header(BaseModel):
    accept: str = "application/json"
    api_key: str


class FundList(Header):

    accept_language: enums.AcceptLanguage = enums.AcceptLanguage.he
