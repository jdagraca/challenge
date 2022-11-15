from __future__ import annotations

from pydantic import BaseModel
from typing import Type, TypeVar, List, Optional


Model = TypeVar("Model", bound="BaseModel")


class ObjBase(BaseModel):
    class Config:
        allow_population_by_field_name = True

    @classmethod
    def map_from_obj(cls: Type["Model"], obj: BaseModel) -> Optional[BaseModel]:
        if obj is None:
            return None
        return cls.parse_obj(obj.dict())

    @classmethod
    def map_to_list_dict(cls: Type["Model"], objs: List[BaseModel]):
        result = []
        for i in range(len(objs)):
            result.append(cls.map_from_dict(objs[i]))

        return result

    @classmethod
    def map_from_dict(cls: Type["Model"], dic: dict):
        return cls.parse_obj(dic)
