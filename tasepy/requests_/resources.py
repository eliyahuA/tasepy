"""URL path extension models for TASE API endpoints.

Provides resource abstraction for constructing endpoint URLs with additional
path parameters using polymorphic design.
"""
from abc import ABC, abstractmethod
from pydantic import BaseModel, computed_field


class IResource(ABC):
    """Abstract interface for generating URL path extensions."""

    @property
    @abstractmethod
    def resource_path(self) -> str:
        pass


class NoResource(BaseModel, IResource):
    """Empty resource for endpoints without path parameters."""

    @property
    def resource_path(self) -> str:
        return ""


class MonthlyDatedResource(BaseModel, IResource):
    """Base resource for year and month path parameters.
    
    Example:
        MonthlyDatedResource(year=2024, month=6)
        # Generates: "/2024/6"
    """
    year: int
    month: int

    @computed_field
    @property
    def resource_path(self) -> str:
        return f"/{self.year}/{self.month}"


class DatedResource(MonthlyDatedResource, IResource):
    """Resource extending MonthlyDatedResource with day parameter.
    
    Uses Progressive Extension Pattern to reuse parent month/year logic
    and append day parameter via super().
    
    Example:
        DatedResource(year=2024, month=6, day=23)
        # Generates: "/2024/6/23"
    """
    day: int

    @computed_field
    @property
    def resource_path(self) -> str:
        return f"{super().resource_path}/{self.day}"


class DatedIndexResource(DatedResource, IResource):
    """Resource extending DatedResource with index_id prefix parameter.
    
    Uses Progressive Extension Pattern to reuse parent date logic
    and prepend index_id parameter via super().
    
    Example:
        DatedIndexResource(index_id=123, year=2024, month=6, day=23)
        # Generates: "/123/2024/6/23"
    """
    index_id: int

    @computed_field
    @property
    def resource_path(self) -> str:
        return f"/{self.index_id}{super().resource_path}"
