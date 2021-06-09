# Your User class goes here
from classes.posts import Posts
import csv
import os

class User:

    def __init__(self, name, email_address, dl_number, account_type):
        self.name = name
        self.email_address = email_address
        self.dl_number = dl_number
        self.account_type = account_type


    def __str__(self):
        return f'\n{self.name}\nAccount Type: {self.account_type}\n-email: {self.email_address}\nDL number: {self.dl_number}\n'
        
    @classmethod
    def objects(cls):
        users = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/users.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                users.append(User(**dict(row)))

        return users

class PremiumUser(User):
    def __init__(self, name, email_address, dl_number, account_type):
        super().__init__(self, name, email_address, dl_number, account_type)

class FreeUser(User):
    def __init__(self, name, email_address, dl_number, account_type):
        super().__init__(self, name, email_address, dl_number, account_type)


