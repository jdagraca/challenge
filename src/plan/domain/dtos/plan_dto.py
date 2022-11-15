from pydantic import Field, validator
from src.utils.obj_base import ObjBase
from src.utils.db_base import DbBase
from src.utils.oid import OID
from typing import Optional


class PlanDto(ObjBase, DbBase):
    id: Optional[OID]
    precio: Optional[float] = Field(alias="precio")

    @validator("precio")
    @classmethod  # Optional, but your linter may like it.
    def check_tipo_type(cls, value):
        if value < 0:
            raise ValueError("Percio Plano no puede ser 0")
        return value
