import mlab
from movie import Movie
from resource import Resource

from faker import Faker

from random import randint


faker = Faker("en_US")

mlab.connect()

#  ----------------  Delete  ----------------------
# m = Movie.objects().with_id("5bf8018ee7179a56e2155336")
# print(m.title)
# m.delete()

#------------------- Read  ------------------------
# m = Movie(title = 'Batman', year = 2005, image = 'https://images-na.ssl-images-amazon.com/images/I/41trnBjzshL.jpg')
# m.save()
# moive_list = Movie.objects()
# for m in moive_list:
#     print(m.title)


# r = Resource(name = 'Quan', city = 'Russia', yob = 1995, height = 175, weight = 70)
# r.save()
# resource_list = Resource.objects()
# for r in resource_list:
#     print(r.name, r.yob, r. city)


# -------- Xoa phan tu dau tien hoac cuoi cung ---------------
# r = Resource.objects().first()
# print(r)

# resource_list = Resource.objects()
# last_id = len(resource_list) - 1
# print(resource_list[last_id].id)
# resource_list[last_id].delete()
# print(resource_list[0].id)

# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953, 2000)
#     height = randint(150, 190)
#     weight = randint(40, 120)
#     r = Resource(name = name, city = city, yob = yob, height = height, weight = weight)
#     r.save()

# records = Resource.objects(height = 172)
# for r in records: 
#     print('name :', r.name, ' - city :', r.city)


# http://docs.mongoengine.org/guide/querying.html
records = Resource.objects(height__gt=155, weight__gt=50, name__icontains="a", height__lt=165)
print(len(records))


# ----------------------- Update 1 truong available voi gia tri False
# records = Resource.objects()
# for r in records:
#     r.update(set__available=False)

# r = Resource.objects().with_id("5bf80cbb6eca8803809c887d")
# r.update(set__available=True)