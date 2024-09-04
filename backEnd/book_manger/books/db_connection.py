import pymongo    # Interact directly with MongoDB Collections 

url = 'mongodb+srv://DBuser:k9W7qC9opqf3SlZB@cluster0.nbryfya.mongodb.net/'
client = pymongo.MongoClient(url )

db = client['BookManger_db']
books_collection = db['books_db']
user_collection = db['users']