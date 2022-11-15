from __future__ import annotations

from typing import Type, TypeVar, Optional

from pydantic import BaseModel

Model = TypeVar("Model", bound="BaseModel")


class DbBase(BaseModel):
    @classmethod
    def map_from_orm(cls: Type["Model"], obj) -> Optional[BaseModel]:
        if obj is None:
            return None

        return cls.from_orm(obj)

    @classmethod
    def map_to_list_orm(cls: Type["Model"], objs):
        result = []
        for i in range(len(objs)):
            result.append(cls.map_from_orm(objs[i]))
        return result

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
