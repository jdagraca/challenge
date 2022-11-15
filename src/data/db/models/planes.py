from mongoengine import Document, DecimalField


class Plan(Document):
    precio = DecimalField()
