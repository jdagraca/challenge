from src.socio.domain.daos.socio_dao import SocioDao
from src.socio.domain.entity.socio import SocioDomain


class SocioService:
    def __init__(self):
        self._socio_dao = SocioDao()
        pass

    def extender_vigencia(self, socio_id):
        socio = SocioDomain.map_from_obj(self._socio_dao.get_socio(socio_id))
        socio.extender_vigencia()

        new_fecha = dict()
        new_fecha["fecha_vigencia"] = socio.fecha_vigencia

        self._socio_dao.update_socio(socio_id, new_fecha)

    def get_socio(self, socio_id):
        return self._socio_dao.get_socio(socio_id)

    def get_descuentos_habilitados(self, socio_id) -> list:
        socio = SocioDomain.map_from_obj(self._socio_dao.get_socio(socio_id))
        descuentos = socio.get_descuentos_disponibles()
        return descuentos

    def get_socios_activos(self):
        filtros = dict()
        filtros["estado"] = "activo"
        return self._socio_dao.get_socios(filtros)
