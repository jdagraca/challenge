from datetime import date
from typing import List
from typing import Optional

from pydantic import Field

from src.descuento.domain.entity.descuento import DescuentoDomain
from src.utils.date_utils import incrementar_mes
from src.utils.obj_base import ObjBase
from src.utils.oid import OID


class PagosDomain(ObjBase):
    id: Optional[OID]
    socio_id: Optional[OID] = Field(alias="socio_id")
    monto: Optional[float] = Field(alias="monto")
    periodo_desde: Optional[date] = Field(alias="periodo_desde")
    periodo_hasta: Optional[date] = Field(alias="periodo_hasta")
    descuentos_aplicados: Optional[List[OID]] = Field(alias="descuentos_aplicados")

    def set_periodo(self, fecha_vigencia: date):
        self.periodo_desde = fecha_vigencia
        self.periodo_hasta = incrementar_mes(fecha_vigencia, 1)

    def set_monto(self, descuentos: List[DescuentoDomain], precio_plan: float) -> float:
        descuentos_list = list()
        importe = precio_plan
        for d in descuentos:
            self._validar_tipo_descuento(d.tipo)
            descuentos_list.append(d.id)
            if d.tipo == "absoluto":
                importe -= d.monto
            if d.tipo == "porcentual":
                self._validar_monto_porcentual_descuento(d.monto)
                importe -= precio_plan * d.monto
        if importe < 0:
            importe = 0
        self.descuentos_aplicados = descuentos_list
        return importe

    def _validar_tipo_descuento(self, tipo: str):
        if tipo not in ["porcentual", "absoluto"]:
            raise ValueError("Tipo Descuento Invalido")

    def _validar_monto_porcentual_descuento(self, monto: float):
        if monto >= 1.0:
            raise ValueError("Descuento Porcentual no puede ser mayor al %100")
