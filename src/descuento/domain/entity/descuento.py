from typing import Optional

from pydantic import Field

from src.utils.obj_base import ObjBase
from src.utils.oid import OID


class DescuentoDomain(ObjBase):
    id: Optional[OID]
    monto: Optional[float] = Field(alias="monto")
    tipo: Optional[str] = Field(alias="tipo")
    cantidad_aplicaciones: Optional[int] = Field(alias="cantidad_aplicaciones")

    def validar_disponibilidad(self) -> bool:
        if self.cantidad_aplicaciones >= 1:
            return True
        else:
            return False

    def descontar_aplicacion(self) -> bool:
        if self.validar_disponibilidad():
            self.cantidad_aplicaciones -= 1
            return True
