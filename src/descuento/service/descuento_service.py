from src.descuento.domain.daos.descuento_dao import DescuentosDao
from src.descuento.domain.entity.descuento import DescuentoDomain


class DescuentoService:
    def __init__(self):
        self._descuento_dao = DescuentosDao()
        pass

    def descontar_aplicacion(self, descuentos_aplicar: list):
        for des in descuentos_aplicar:
            descuento_domain = DescuentoDomain.map_from_obj(des)
            descuento_update = dict()
            descuento_update[
                "cantidad_aplicaciones"
            ] = descuento_domain.descontar_aplicacion()
            self._descuento_dao.update_descuento(descuento_domain.id, descuento_update)
