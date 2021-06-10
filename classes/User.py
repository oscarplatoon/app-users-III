# from classes.interface import Interface
import csv
import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/userdata.csv")

my_path = os.path.abspath(os.path.dirname(__file__))
path_post = os.path.join(my_path, "../data/post.csv")


class User:
    users = []
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_user(self, user_data): # None       
        User.users.append(user_data)
        with open(path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["username", "password", "membership"])
            writer.writeheader()
            for row in User.users:
                writer.writerow(row) 

    def add_post(self, content):
        with open(path_post, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(content)
        