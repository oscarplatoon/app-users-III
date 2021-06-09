import csv
import os

class Posts:

     def __init__(self, post_id):
         self.post_id = post_id

     @classmethod
     def post_objects(cls):
         post_list = {}
         my_path = os.path.abspath(os.path.dirname(__file__))
         path = os.path.join(my_path, "../data/posts.csv")
         with open(path) as csvfile:
             reader = csv.reader(csvfile)
             for row in reader:
                 post_list[row[0]] = row[1:]

         return post_list