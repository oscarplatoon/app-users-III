
from .User import User
# Requirement 
# Add a method to your User class that allows for creating a new user post.
# Add any necessary instance properties to make step 1 work. What data structure should you use?
# Add a class variable that stores the posts from every user. What data structure should you use?
# Make sure that the the information stays in sync!

# Pseudocode
# Created an interface that makes a new user
# runner is init interface to run and outputs menu while true
# give the user an input option to create a new user
# 

class Interface:
    def __init__(self):
        pass
        # self.create_user = User(user_data)
        
    def run(self):
        while True:
            mode = int(input("\n1: Create new User\n2: Write new Post\n3: Quit application\n\n"))

            if mode == 1:
                user_data = {}
                user_data['role'] = 'user'
                user_data['name'] = input("Enter your name:\n")
                user_data['email'] = input("Enter your email:\n")
                user_data['password'] = input("Create a password:\n")
                user_data['membership'] = input("Type 'premium' to gain access to more features!")
                User.add_user(self, user_data)

            elif mode == 2:
                content = []
                content.append(input('Enter new post:\n'))
                User.add_post(self, content)
            
            elif mode == 3:
                return
