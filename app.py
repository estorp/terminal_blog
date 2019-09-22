# import pymongo

# uri = "mongodb://127.0.0.1:27017"

# client = pymongo.MongoClient(uri)
# database = client['fullstack']
# collection = database['ews']

# students = collection.find({})
# for student in students:
#   print(student)

# List Comprehension
# students = [ student['name'] for student in collection.find({}) if student['mark'] >= 80 ]
# students = [ student['mark'] for student in collection.find({}) ]
# print(type(students))
# print(type(students[1]))

# OOP
# Python Package -- models
from database import Database
from models.post import Post

Database.initialize()

post = Post("Post1 Title", "Post1 content", "Post1 author")
post2 = Post("Post2 Title", "Post2 content", "Post2 author")

# post2.content = "Somehow a new content"

print(post.content)
print(post2.content)