import csv 
import os.path

from classes.User import User
from classes.Post  import Posts

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/user_info.csv")
user_info_path = os.path.join(my_path, "../data/user_info.csv")

class Interface():
    def __init__(self):
        self.users = User.all_users()
        self.posts = Posts.all_posts()
        self.login_menu()


    def login_menu(self):
        while True:
            user_input = int(input("""

            1. Create account\n
            2. Login\n
            3. Quit

            """))
            if user_input == 1:
                self.add_user()
            elif user_input == 2:
                self.login()
            elif user_input == 3:
                break

    def main_menu(self):

        while True:
            # input = self.menu()
            try:
                user_input = int(input("""
                
                1. View users
                2. Delete user
                3. View all posts
                4. View my posts
                5. Add Post
                6. Quit
                
                """))
            
                if user_input == 1:
                    self.view_users()
                elif user_input == 2:
                    self.delete_user()
                elif user_input == 3:
                    self.view_all_posts()
                elif user_input == 4:
                    self.view_my_posts()
                elif user_input == 5:
                    self.add_post()
                elif user_input == 6:
                    self.logged_in_user = None
                    self.loggedIn = False
                    break
            except:
                print('Please select options 1-6')
                self.main_menu()


    # def menu(self):
    #     return int(input("1. Add user\n2. Add post\n3. View Users\n4. Quit\n> "))

    def add_user(self):

        user_data = {'name': 'user'}

        user_data['name'] = input('please enter your name: \n')
        user_data['email'] = input('please enter your email: \n')
        user_data["drivers_license"] = input('Please enter your drivers lisence number: \n')
        user_data['is_premium'] = 'True'if input('Would you like to pay for Premium Membership y/n?: \n') == 'y' else 'False'
    
        self.users.append(User(**dict(user_data)))
        with open(user_info_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["name", "email", "drivers_license", "is_premium"])
            writer.writeheader()
            for user in self.users:
                name=user.name
                email=user.email
                drivers_license=user.drivers_license
                is_premium = user.is_premium
                writer.writerow({'name': name,'email': email, 'drivers_license': drivers_license,'is_premium': is_premium})

        print(f"congradulations {user_data['name']} you have successfully created an account!")

    def login(self):
        drivers_license = input('Please enter your drivers lisence number: \n')
        for user in User.all_users():
            if user.drivers_license == drivers_license:
                self.logged_in_user = user
                self.all_users = User.all_users()
                self.logged_in = True
                self.all_posts = Posts.all_posts()
                return self.main_menu()
        print(f"\n\nUser with drivers license number {drivers_license} not found.\n\nPlease try again.")        
        self.login_menu

    def view_users(self):
        # users = User.all_users()
        for user in self.users:
            print(f"Name: {user.name}, Email Address: {user.email}, Driver's License: {user.drivers_license}")

    def delete_user(self):
        delete_drivers_license = input('What is the Drivers Lisence Number of the user you would like to delete: \n')
        with open(user_info_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["name", "email", "drivers_license", "is_premium"])
            writer.writeheader()
            for user in self.users:
                # print (user.drivers_license)
                # print (drivers_license)
                if user.drivers_license != delete_drivers_license:
                    name=user.name
                    email=user.email
                    drivers_license=user.drivers_license
                    is_premium = user.is_premium
                    writer.writerow({'name': name,'email': email, 'drivers_license': drivers_license,'is_premium': is_premium})
                

    def view_all_posts(self):
        for posts in self.all_posts:
            print (posts.post)

    def view_my_posts(self):
        for posts in self.all_posts:
            if posts.name == self.logged_in_user.name:
                print (posts.post)

    def add_post(self):
        post_data = {'name': 'user'}

        post_data['name'] = self.logged_in_user.name
        post_data['post'] = input('Your post here: \n')
        
        Posts.add_post(self, post_data)
        


    def view_users(self):
        # users = User.all_users()
        for user in self.users:
            print(f"Name: {user.name}, Email Address: {user.email}, Driver's License: {user.drivers_license}")
