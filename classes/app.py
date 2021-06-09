import csv
import os
from classes.User import User
from classes.posts import Posts

class App:

     def __init__(self, name):
         self.name = name
         self.users = User.objects()
         self.posts = Posts.post_objects()

     def list_users(self):
         print('\n')
         for i, user in enumerate(self.users):
             print(f'{i + 1}. {user.name} {user.email_address}')

     def find_user(self, drivers_num):
         for user in self.users:
             if user.dl_number == drivers_num:
                 return user
         return "User Not Found"

     def add_user(self, user_data):
         self.users.append(User(user_data['name'], user_data['email_address'], user_data['dl_number'], user_data['account_type']))
         self.posts[user_data['dl_number']] = [user_data['dl_number']]
         self.save()

         my_path = os.path.abspath(os.path.dirname(__file__))
         path = os.path.join(my_path, "../data/posts.csv")
         with open(path, 'a') as csvfile:
             writer = csv.writer(csvfile)
             writer.writerow(self.posts[user_data['dl_number']])

     def add_post(self, drivers_id):
         for post in self.posts:
             if drivers_id == post:
                 user_post = input("Enter text for you post: ")
                 self.posts[f'{post}'].append(user_post)
         self.save_posts()

     def save(self):
         my_path = os.path.abspath(os.path.dirname(__file__))
         path = os.path.join(my_path, "../data/users.csv")

         with open(path, 'w') as csvfile:
             user_csv = csv.writer(csvfile, delimiter=',')
             user_csv.writerow(['name', 'email_address', 'dl_number', 'account_type'])
             for user in self.users:
                 user_csv.writerow([user.name, user.email_address, user.dl_number, user.account_type])

     def save_posts(self):
         my_path = os.path.abspath(os.path.dirname(__file__))
         path = os.path.join(my_path, "../data/posts.csv")

         with open(path, 'w') as csvfile:
             writer = csv.writer(csvfile)
             for row in self.posts:
                 self.posts[row].insert(0,row)
                 writer.writerow(post for post in self.posts[row])