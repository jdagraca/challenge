from src.descuento.service.descuento_service import DescuentoService
from src.pago.domain.daos.pago_dao import PagosDao
from src.pago.domain.entity.pago import PagosDomain
from src.plan.service.plan_service import PlanService
from src.socio.service.socio_service import SocioService


class PagoService:
    def __init__(self):
        self._pago_dao = PagosDao()
        self._socios_service = SocioService()
        self._descuento_service = DescuentoService()
        self._plan_service = PlanService()

    def add_pago(self, socio_id, fecha_plan, descuentos, precio_plan):
        pago = PagosDomain()
        pago.socio_id = socio_id
        pago.set_periodo(fecha_plan)
        pago.set_monto(descuentos, precio_plan)
        pago = self._pago_dao.add_pago(PagosDomain.map_from_obj(pago))
        return pago.dict()
