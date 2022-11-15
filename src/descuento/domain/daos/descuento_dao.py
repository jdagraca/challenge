from mongoengine import *

from src.data.cnn.conexiondb import ConexionDB
from src.data.db.models.descuentos import Descuentos
from src.descuento.domain.dtos.descuento_dto import DescuentoDto


class DescuentosDao:
    def __init__(self):
        self._db: connect = ConexionDB.get_db()

    def get_descuento(self, pk) -> DescuentoDto:
        descuento = Descuentos.objects.get(id=pk)
        return DescuentoDto.map_from_orm(descuento)

    def update_descuento(self, descuento_id: str, params: list) -> DescuentoDto:
        descuento = Descuentos.objects(pk=descuento_id).update(**params)
        return DescuentoDto.map_from_orm(descuento)
