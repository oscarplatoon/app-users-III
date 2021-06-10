from classes.User import User

import csv
import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/userdata.csv")

my_path = os.path.abspath(os.path.dirname(__file__))
path_post = os.path.join(my_path, "../data/post.csv")


class FreeUser(User):
    
    def __init__(self, username, password, membership):
        super().__init__(username, password, membership=membership)


    def limited_post(self, content):
        print("--- Free poster ---")
        post_counter = 1           
        while post_counter < 2:
            with open(path_post, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(content)
                input("Enter response: ")
            post_counter += 1
        if post_counter == 2:
            print("\n-------\nThank you for registering for a trial!\n-------\nto continue posting please upgrade your membership!")      