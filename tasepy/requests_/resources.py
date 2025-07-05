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
    year: int
    month: int

    @computed_field
    @property
    def resource_path(self) -> str:
        return f"/{self.year}/{self.month}"


class DatedResource(MonthlyDatedResource, IResource):
    day: int

    @computed_field
    @property
    def resource_path(self) -> str:
        return f"{super().resource_path}/{self.day}"


class DatedIndexResource(DatedResource, IResource):

    index_id: int

    @computed_field
    @property
    def resource_path(self) -> str:
        return f"/{self.index_id}/{super().resource_path}"
