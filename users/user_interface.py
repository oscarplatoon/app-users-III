from users.User import User
from users.Post import Post
from users.FreeUser import FreeUser


class UserInterface():
     def __init__(self):
         self.users = []
         self.all_posts = []
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
                 self.user_post()
             elif input == 5:
                 break

     def menu(self):
         return int(input("1. Add user\n2. Delete User\n3. View Users\n4. New Post\n5. Quit\n> "))

     def add_user(self):
         name = input("Enter user name: ")
         email = input("Enter user email address: ")
         license = input("Enter user Driver's license: ")
         user_tier = input("Enter user Tier((F)ree or (P)remium: ")
         self.users.append(User(name, email, license, user_tier))
         print(f"User {name} added.")

     def delete_user(self):
         license = input("Enter the driver's license number of the user to delete: ")
         for i, user in enumerate(self.users):
             if license == user.get_license():
                 self.users.pop(i)
                 print(f"User with license {license} deleted.")
                 return

         print(f"Unable to find a user with license {license}.")

     def view_users(self):
         for user in self.users:
             print(user)

     def user_post(self):
         user = input("Enter user name to post to: ")
         post = input("What would you like to post? ")
         new_post = Post(post)

         for current_user in self.users:
             if current_user.name == user:
                 self.all_posts.append(new_post)
                 current_user.set_post(new_post)
                 print(f"{current_user.name} successfully posted")
                 return

         print(f"Unable to post to {user}")    
