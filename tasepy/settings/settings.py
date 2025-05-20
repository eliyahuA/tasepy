from pydantic import BaseModel


class ApiKeyFile(BaseModel):
    key: str


class Settings(BaseModel):
    api_key: str

