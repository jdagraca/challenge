from datetime import date
from typing import List
from typing import Optional

from pydantic import Field

from src.descuento.domain.dtos.descuento_dto import DescuentoDto
from src.plan.domain.dtos.plan_dto import PlanDto
from src.utils.db_base import DbBase
from src.utils.obj_base import ObjBase
from src.utils.oid import OID


class SocioDto(ObjBase, DbBase):
    id: Optional[OID]
    nombre: Optional[str] = Field(alias="nombre")
    plan_id: Optional[PlanDto] = Field(alias="plan_id")
    estado: Optional[str] = Field(alias="estado")
    fecha_vigencia: Optional[date] = Field(alias="fecha_vigencia")
    discount: Optional[List[DescuentoDto]] = Field(alias="discount")
