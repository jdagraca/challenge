from mongoengine import Document, ReferenceField, DateField, StringField, ListField

from src.data.db.models.descuentos import Descuentos
from src.data.db.models.planes import Plan

ESTADOS = ("activo", "inactivo")


class Socio(Document):
    nombre = StringField()
    plan_id = ReferenceField(Plan)
    estado = StringField(choices=ESTADOS)
    fecha_vigencia = DateField()
    discount = ListField(ReferenceField(Descuentos))
