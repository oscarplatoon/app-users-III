# Import and create your users herefrom classes.app import App
from classes.app import App
from classes.User import User
from classes.User import FreeUser
from classes.User import PremiumUser

app = App("Eric's App")
mode = ''


while mode != '5':
     mode = input("\nWhat would you like to do?\nOptions:\n1. Add a User\n2. List Users\n3. Add a Post\n5. Quit\n")
     if mode == '1':
         user_data = {}
         user_data['name'] = input("Enter your name: ")
         user_data['email_address'] = input("Enter your email address: ")
         user_data['dl_number'] = input("Enter your driver's license number: ")
         user_data['account_type'] = input("Would you like a free or Premium Account?: ")
         app.add_user(user_data)
         

     elif mode == '2':
         app.list_users()
     elif mode == '3':
         drivers_id = input("Enter driver's license number: ")
         app.add_post(drivers_id)

     elif mode == '5':
         break
     else:
         pass