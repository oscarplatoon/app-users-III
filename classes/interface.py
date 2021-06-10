from classes.PremiumUser import PremiumUser
from classes.FreeUser import FreeUser
from classes.User import User

# ----app user 2   
# Add a method to your User class that allows for creating a new user post.
# Add any necessary instance properties to make step 1 work. What data structure should you use?
# Add a class variable that stores the posts from every user. What data structure should you use?
# Make sure that the the information stays in sync!

# Your User class goes here
# # 1. Your `User` class will now become a base class.
# 2. Create two subclasses `PremiumUser` and `FreeUser` that will inherit from `User`.
# 3. Override the `add_post` method for `FreeUser` so that an instance of `FreeUser` is only able to make two posts.
# 4. In the `runner.py` file, import `FreeUser` and `PremiumUser` and create at least one instance of each.
# 5. Add tests.

"""
Pseudo code 
--- step 1
* User is a base class *
*`FreeUser` = child of user * - option 1
* 'Pemium user = child of user 
****************

* free user limited to 2 posts each.

* `PremiumUser` = grandchild of user & child of freeuser *
* Ammend interface - create new user makes a free user account


--- step 2
* `FreeUser` - Override `add_post` and add post limit = 2
* PremiumUser` - unlimited posts



--- final step
* `runner.py` - import `FreeUser` - use try and raise exception
* `runner.py` - `PremiumUser`
"""

class Interface:
    
    def __init__(self):
        pass

    def login(self, membership = None):
        self.membership = membership
        self.menu()

    def menu(self):
        print("Welcome, please log in")
        mode = int(input("\n1: Login \n2: Quit application\n"))
        if mode == 1:
            user_data = {}
            user_data['username'] = input("Enter your user name:\n")
            user_data['password'] = input("Enter your password:\n")
            User.add_user(self, user_data)
            self.logged_in = True
            self.logged_in_menu()     
        elif mode == 2:
            return
    
    def logged_in_menu(self):
        while self.logged_in == True:
            print(f"\n\n----- Thank you for logging in -----\n")
            mode = int(input("What would you like to do?\n\n1: Write new post\n2: Logout\n"))
            if mode == 1:
                content = []
                content.append(input('Enter new post:\n'))
                if self.membership == None:
                    FreeUser.add_post(self, content)
                else:
                    PremiumUser.add_post(self, content)
            
            elif mode == 2:
                print("\nGoodbye!\n")
                return
    