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


class DatedIndexResource(BaseModel, IResource):
    """Resource for index component endpoints with date parameters.
    
    Example:
        DatedIndexResource(index_id=123, year=2024, month=6, day=23)
        # Generates: "/123/2024/6/23"
    """
    index_id: int
    year: int
    month: int
    day: int

    @computed_field
    @property
    def resource_path(self) -> str:
        return f"/{self.index_id}/{self.year}/{self.month}/{self.day}"
