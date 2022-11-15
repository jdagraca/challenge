from mongoengine import Document, DecimalField, IntField, StringField

DESCUETNOS_TIPOS = ("porcentual", "absoluto")


class Descuentos(Document):
    monto = DecimalField()
    tipo = StringField(choices=DESCUETNOS_TIPOS)
    cantidad_aplicaciones = IntField()
