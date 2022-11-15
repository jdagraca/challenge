from mongoengine import Document, DateField, DecimalField, ReferenceField, ListField
from src.data.db.models.descuentos import Descuentos
from src.data.db.models.socios import Socio


class Pagos(Document):
    socio_id = ReferenceField(Socio)
    monto = DecimalField()
    periodo_desde = DateField()
    periodo_hasta = DateField()
    descuentos_aplicados = ListField(ReferenceField(Descuentos))
