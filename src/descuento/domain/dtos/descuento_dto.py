from pydantic import Field, validator
from src.utils.obj_base import ObjBase
from src.utils.db_base import DbBase
from src.utils.oid import OID
from typing import Optional


class DescuentoDto(ObjBase, DbBase):
    id: Optional[OID]
    monto: Optional[float] = Field(alias="monto")
    tipo: Optional[str] = Field(alias="tipo")
    cantidad_aplicaciones: Optional[int] = Field(alias="cantidad_aplicaciones")
