from mongoengine import *

from src.data.cnn.conexiondb import ConexionDB
from src.data.db.models.socios import Socio
from src.socio.domain.dtos.socio_dto import SocioDto


class SocioDao:
    def __init__(self):
        self._db: connect = ConexionDB.get_db()

    def get_socio(self, pk) -> SocioDto:
        socio = Socio.objects.get(pk=pk)
        return SocioDto.map_from_orm(socio)

    def update_socio(self, socio_id, params) -> int:
        socio = Socio.objects(pk=socio_id).update(**params)
        return socio

    def get_socios(self, params) -> int:
        socios = Socio.objects(**params)
        return SocioDto.map_to_list_orm(socios)
