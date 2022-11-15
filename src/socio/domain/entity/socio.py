from datetime import date
from typing import List
from typing import Optional

from pydantic import Field

from src.descuento.domain.entity.descuento import DescuentoDomain
from src.plan.domain.dtos.plan_dto import PlanDto
from src.utils.date_utils import incrementar_mes
from src.utils.db_base import DbBase
from src.utils.obj_base import ObjBase
from src.utils.oid import OID


class SocioDomain(ObjBase, DbBase):
    id: Optional[OID]
    nombre: Optional[str] = Field(alias="nombre")
    plan_id: Optional[PlanDto] = Field(alias="plan_id")
    estado: Optional[str] = Field(alias="estado")
    fecha_vigencia: Optional[date] = Field(alias="fecha_vigencia")
    discount: Optional[List[DescuentoDomain]] = Field(alias="discount")

    def extender_vigencia(self):
        self.fecha_vigencia = incrementar_mes(self.fecha_vigencia, 1)

    def get_descuentos_disponibles(self) -> list:
        descuentos_disponibles = list()
        for d in self.discount:
            if d.validar_disponibilidad():
                descuentos_disponibles.append(d)
        return descuentos_disponibles
