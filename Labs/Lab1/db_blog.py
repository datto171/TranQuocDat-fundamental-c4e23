from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. ket noi 
client = MongoClient(uri)

#2. lay ra database mac dinh 
db = client.get_database()

#3. lay ra collection
posts = db["posts"] # lazy loading
movie = db["movie"]

#4. tao data
new_posts = {
    "title": "hom nay troi nang",
    "content": "Toi o nha choi dien tu",
}

new_movie = {
    "title": "death note",
    "rating": "6.5",
}

#5. them data
# posts.insert_one(new_posts)
# movie.insert_one(new_movie)

#5. read data
post_list = posts.find()
# for i in post_list:
#     print(i)
p = post_list[0]
print(p["title"])
print(p["content"])

#6 dong connect
client.close()