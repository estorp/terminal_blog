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
# from models.post import Post
from models.blog import Blog

Database.initialize()

blog = Blog(author="Tito Sotto",
            title="Tito Sotto Title Sample",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())

# post = Post(blog_id='12039847',
#             title='Guide to sleeping very well',
#             content='Never to sleep so soon before you eat',
#             author='Vic Sotto')
# post.save_to_mongo()

# post = Post.from_mongo('65bebe4d83004f1c8030bf2c521655ed')
# print(post)

# posts = Post.from_blog('12039847')
# for post in posts:
#   print(post)

# post = Post("Post1 Title", "Post1 content", "Post1 author")
# post2 = Post("Post2 Title", "Post2 content", "Post2 author")

# post2.content = "Somehow a new content"

# print(post.content)
# print(post2.content)