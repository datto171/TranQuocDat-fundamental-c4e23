from mongoengine import Document, StringField

class Register(Document):
  meta = {
    "strict": False
  }
  username = StringField()
  password = StringField()
  email = StringField()