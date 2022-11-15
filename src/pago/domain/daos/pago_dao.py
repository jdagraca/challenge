from mongoengine import connect

from src.data.cnn.conexiondb import ConexionDB
from src.data.db.models.pagos import Pagos
from src.pago.domain.dtos.pago_dto import PagosDto


class PagosDao:
    def __init__(self):
        self._db: connect = ConexionDB.get_db()

    def add_pago(self, pago_dto: PagosDto) -> PagosDto:
        pago = Pagos(**pago_dto.dict())
        pago.save()
        pago.socio_id = pago.socio_id.id

        return PagosDto.map_from_orm(pago)
