from Post import Post
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "users.csv")


class User:
  all_posts = []

  def __init__(self, name, email_address, driver_license):
    self.name = name
    self.email_address = email_address
    self.driver_license = driver_license
    self.user_posts = []

  @classmethod
  def get_all_users(cls):
    with open(path, 'r') as users_file:
      users = csv.DictReader(users_file)
      users_list = []
      for user in users:
        new_user = User(user['name'], user['email_address'], user['driver_license'])
        users_list.append(new_user)
      return users_list


  # def create_post(self, title, body):
  #   new_post = Post(self.driver_license, title, body)
  #   self.user_posts.append(new_post)


