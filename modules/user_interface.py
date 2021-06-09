from modules.User import User
from modules.post import Post
from modules.FreeUser import FreeUser
from modules.PremiumUser import PremiumUser

class UserInterface():
    def __init__(self):
        self.users = []
        self.all_posts = []
        self.run()

    def run(self):

        while True:
            input = self.menu()
            if input == 1:
                self.add_free_user()
            elif input == 2:
                self.add_premium_user()
            elif input == 3:
                self.delete_user()
            elif input == 4:
                self.view_users()
            elif input == 5:
                self.user_post()
            elif input == 6:
                break
    
    def menu(self):
        return int(input("1. Add Free user\n2. Add Premium user\n3. Delete User\n4. View Users\n5. New Post\n6. Quit\n> "))
    
    def add_free_user(self):
        name = input("Enter user name: ")
        email = input("Enter user email address: ")
        license = input("Enter user Driver's license: ")
        self.users.append(FreeUser(name, email, license))
        print(f"Free User {name} added.")

    def add_premium_user(self):
        name = input("Enter user name: ")
        email = input("Enter user email address: ")
        license = input("Enter user Driver's license: ")
        self.users.append(PremiumUser(name, email, license))
        print(f"Premium User {name} added.")
    
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
                try:
                    current_user.set_post(new_post)
                    self.all_posts.append(new_post)
                    print(f"{current_user.name} successfully posted")
                    return
                except Exception as e:
                    print(e)
                    return

        print(f"Unable to post {user} not found")    
        

    