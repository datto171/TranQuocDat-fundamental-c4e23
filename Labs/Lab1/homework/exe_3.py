from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. ket noi 
client = MongoClient(uri)

#2. lay ra database mac dinh 
db = client.get_database()

#3. lay ra collection
posts = db["posts"] # lazy loading

#4. tao data
new_posts = {
    "title": "hom nay toi buon",
    "author": "Tran Quoc Dat",
    "content": "cam thay day la mot moi truong tot",
}

#5. them data
posts.insert_one(new_posts)

# post_list = posts.find()
# for i in post_list:
#     print(i)

#6 dong connect
client.close()