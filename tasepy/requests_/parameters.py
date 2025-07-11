from pydantic import BaseModel, Field, ConfigDict, model_validator
from pydantic.alias_generators import to_camel
from typing import Optional

from . import enums


class BaseParameters(BaseModel):
    """Base model for TASE API request parameters.
    
    Provides parameter validation and serialization for API requests.
    Converts Python snake_case field names to camelCase for API compatibility.
    Handles data cleaning and JSON serialization.
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        serialize_by_alias=True,
    )

    @model_validator(mode='before')
    @classmethod
    def remove_none_values(cls, data):
        """Remove None values from input data before model validation.
        
        Prevents None values from being included in API request parameters,
        which could cause API failures or unexpected behavior.
        
        Args:
            data: Input data dictionary or other format
            
        Returns:
            Cleaned data with None values removed
        """
        if isinstance(data, dict):
            return {k: v for k, v in data.items() if v is not None}
        return data

    def model_dump(self, *args, **kwargs):
        """Serialize model to dictionary with API parameter formatting.
        
        Forces JSON serialization mode and applies camelCase field name conversion
        for TASE API compatibility. JSON mode ensures consistent serialization of
        enums, dates, and other complex types without requiring callers to specify mode.
        
        Args:
            *args, **kwargs: Standard Pydantic model_dump arguments
            
        Returns:
            Dictionary with camelCase field names suitable for API requests
        """
        kwargs['mode'] = 'json'
        return super().model_dump(*args, **kwargs)


class FundList(BaseParameters):
    """Parameters for fund list API requests.
    
    Extends BaseParameters to include fund-specific filtering options.
    Defaults to active funds when no listing status is specified.
    """

    listing_status_id: enums.ListingStatusId = Field(
        default=enums.ListingStatusId.Active
    )


class Index(BaseParameters):
    """Parameters for indices online last rate API requests.

    Supports optional filtering by index ID.
    """
    index_id: Optional[int] = None


class IndexWithTime(Index):
    """Parameters for indices online intraday API requests.
    
    Supports optional filtering by index ID and start time.
    """

    start_time: Optional[str] = None
