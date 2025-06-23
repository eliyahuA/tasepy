from abc import ABC, abstractmethod
from pydantic import BaseModel, computed_field
from typing import Optional


class IResource(ABC):

    @property
    @abstractmethod
    def resource_path(self) -> str:
        pass


class NoResource(BaseModel, IResource):

    @property
    def resource_path(self) -> str:
        return ""


class DatedIndexResource(BaseModel, IResource):
    index_id: int
    year: int
    month: int
    day: int

    @computed_field
    @property
    def resource_path(self) -> str:
        return f"/{self.index_id}/{self.year}/{self.month}/{self.day}"
