from pydantic import BaseModel


class ApiKeyFile(BaseModel):
    """Validates and parses API key from YAML configuration files.
    """
    key: str


class Settings(BaseModel):
    """Core configuration for TASE DataWise API client.
    
    Contains authentication credentials and configuration settings
    used by all API client operations.
    """
    api_key: str

