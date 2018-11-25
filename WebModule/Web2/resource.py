from mongoengine import Document, StringField, IntField,FloatField, BooleanField

class Resource(Document):
    meta = {
        "strict": False
    }
    name = StringField()
    yob = IntField()
    height = FloatField()
    weight = FloatField()
    available = BooleanField(default=False)