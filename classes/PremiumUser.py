# Your PremiumUser class goes here
from .User import User
import os
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/userdata.csv")

my_path = os.path.abspath(os.path.dirname(__file__))
path_post = os.path.join(my_path, "../data/post.csv")

class PremiumUser(User):

    def add_user(self, user_data): # None
        User.users.append(user_data)
        print(user_data)
        with open(path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["role", "name", "email", "password"])
            writer.writeheader()
            for row in User.users:
                writer.writerow(row)

    def add_post(self, content):
        print("--- Premium poster ---\n")
        with open(path_post, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(content)
            # print(content)


