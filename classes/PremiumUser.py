import csv
import os

from classes.User import User

my_path = os.path.abspath(os.path.dirname(__file__))
user_post_path = os.path.join(my_path, "../data/user_post.csv")

class PremiumUser(User):

    def __init__(self, name, email, drivers_license):
        super().__init__(name, email, drivers_license)