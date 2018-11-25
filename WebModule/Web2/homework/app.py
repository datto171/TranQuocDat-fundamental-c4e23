import mlab
from faker import Faker
from river import River
from random import randint

mlab.connect()

# http://docs.mongoengine.org/guide/querying.html

# Ex 2
records = River.objects(continent__icontains="Africa")
for r in records:
    print(r.name)

# Ex 3
records = River.objects(continent__icontains="S. America", length__lt=1000)
for r in records:
    print(r.name)