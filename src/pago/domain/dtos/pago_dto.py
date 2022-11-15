from datetime import date
from typing import List, Optional

from pydantic import Field

from src.descuento.domain.dtos.descuento_dto import DescuentoDto
from src.utils.db_base import DbBase
from src.utils.obj_base import ObjBase
from src.utils.oid import OID


class PagosDto(ObjBase, DbBase):
    id: Optional[OID]
    socio_id: Optional[OID] = Field(alias="socio_id")
    monto: Optional[float] = Field(alias="monto")
    periodo_desde: Optional[date] = Field(alias="periodo_desde")
    periodo_hasta: Optional[date] = Field(alias="periodo_hasta")
    descuentos_aplicados: Optional[List[DescuentoDto]] = Field(
        alias="descuentos_aplicados"
    )
