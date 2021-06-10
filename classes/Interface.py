import csv 
import os.path

from classes.User import User

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/user_info.csv")

class Interface():
    def __init__(self):
        self.users = User.all_users()
        self.run()

    def run(self):

        while True:
            input = self.menu()
            if input == 1:
                self.add_user()
            elif input == 2:
                self.delete_user()
            elif input == 3:
                self.view_users()
            elif input == 4:
                self.add_post()
            elif input == 5:
                break

    def menu(self):
        return int(input("1. Add user\n2. Add post\n3. View Users\n4. Quit\n> "))

    def add_user(self):

        user_data = {'name': 'user'}

        user_data['name'] = input('please enter your name: \n')
        user_data['email'] = input('please enter your email: \n')
        user_data["drivers_license"] = input('Please enter your drivers lisence number: \n')

        User.add_user(self, user_data)

        print(f"congradulations {user_data['name']} you have successfully created an account!")


    
    def add_post():
        post = input('Your post here:\n')
        User.add_post(self, post)
        


    def view_users(self):
        for user in self.users:
            print(f"Name: {user.name}, Email Address: {user.email}, Driver's License: {user.drivers_license}")
    # def add_post():