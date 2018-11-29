from mongoengine import Document, StringField, IntField

class Bike(Document):
    model = StringField()
    dailyfee = IntField()
    image = StringField()
    year = IntField()