from mongoengine import Document, StringField, IntField,FloatField

class Movie(Document):
    title = StringField()
    image = StringField()
    year = IntField()