from pydantic import BaseModel, ConfigDict, model_validator
from . import enums


class Header(BaseModel):
    """Base HTTP header model for TASE API requests.
    
    Provides HTTP header abstraction with authentication and proper formatting.
    Handles field transformation from Python snake_case to HTTP kebab-case format.
    Includes security features for API key masking in logs.
    """

    model_config = ConfigDict(
        alias_generator=lambda field_name: field_name.replace("_", "-"),
        populate_by_name=True,
        serialize_by_alias=True,
    )

    accept: str = "application/json"
    apikey: str

    @model_validator(mode='before')
    @classmethod
    def remove_none_values(cls, data):
        """Remove None values from input data before model validation.
        
        Prevents None values from being included in HTTP headers, which could
        cause API request failures. Runs as a pre-validation hook.
        
        Args:
            data: Input data dictionary or other format
            
        Returns:
            Cleaned data with None values removed
        """
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return data

    def model_dump(self, *args, mask: bool = False, **kwargs):
        """Serialize model to dictionary with HTTP header formatting.
        
        Forces JSON serialization mode and provides security masking for API keys.
        Works with alias_generator to convert Python field names to HTTP header format.
        JSON mode ensures consistent serialization of enums and other complex types
        without requiring callers to specify mode.
        
        Args:
            mask: If True, replaces API key with asterisks for secure logging
            *args, **kwargs: Standard Pydantic model_dump arguments
            
        Returns:
            Dictionary with properly formatted HTTP headers
        """
        kwargs['mode'] = 'json'
        data = super().model_dump(*args, **kwargs)
        if mask:
            data['apikey'] = "*"*len(data['apikey'])
        return data


class LanguageAble(Header):
    """Extended header model with language preference support.
    
    Adds accept_language field for API calls requiring language-specific responses.
    Defaults to Hebrew (he-IL) for TASE API compatibility.
    """
    accept_language: enums.AcceptLanguage = enums.AcceptLanguage.he
