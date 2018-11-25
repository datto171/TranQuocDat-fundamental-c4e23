from mongoengine import Document, StringField, IntField,FloatField

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()