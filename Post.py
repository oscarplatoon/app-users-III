import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "posts.csv")

class Post:
  def __init__(self, user_id, title, body):
    self.user_id = user_id
    self.title = title
    self.body = body


  @classmethod
  def get_all_posts(cls):
    with open(path, 'r') as posts_file:
      posts = csv.DictReader(posts_file)
      posts_list = []
      for post in posts:
        new_post = Post(post['user_id'], post['title'], post['body'])
        posts_list.append(new_post)
      return posts_list

  def __str__(self):
    return f"""
    Title: {self.title}
    Body: {self.body}
    """
