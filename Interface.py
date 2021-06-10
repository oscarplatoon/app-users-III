from PremiumUser import PremiumUser
from FreeUser import FreeUser
from User import User
from Post import Post

import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
user_path = os.path.join(my_path, "users.csv")
post_path = os.path.join(my_path, "posts.csv")

class Interface:
  def __init__(self):
    self.logged_in_user = None
    self.loggedIn = False
    self.all_users = []
    self.all_posts = []

  def run(self):
    input = self.start_menu()
    while True:
      if input == 1:
        self.add_user()
        break
      elif input == 2:
        self.login()
        break
      elif input == 3:
        print('Good bye!')
        break

  def authenticated_menu(self):
    while self.loggedIn:
      print("""
      You're logged in!
      """)
      input = self.main_menu()
      if input == 1:
          self.view_users()
      elif input == 2:
          self.delete_user()
      elif input == 3:
          self.view_all_posts()
      elif input == 4:
          self.view_users_posts()
      elif input == 5:
          self.add_post()
      elif input == 6:
          self.logged_in_user = None
          self.loggedIn = False
          break
      elif input == 7:
          self.upgrade_account()
          break

  def start_menu(self):
    return int(input("""
      1. Create user
      2. Login
      3. Exit
    """))

  def main_menu(self):
    return int(input(f"""
      1. View Users
      2. Delete User
      3. View All Posts
      4. View My Posts
      5. Add New Post
      6. Exit
      {'7. Upgrade Account' if self.logged_in_user.tier == 'f' else ''}
    """))

  def upgrade_account(self):
    for idx, user in enumerate(self.all_users):
      if self.logged_in_user.driver_license == user.driver_license:
        self.all_users = self.all_users[:idx] + self.all_users[idx+1:]
        self.all_users.append(PremiumUser(user.name, user.email_address, user.driver_license))
    self.save_users(self.all_users)

  def login(self):
    driver_license = int(input("Please enter your Driver's License number: "))
    for user in Interface.get_all_users_from_db():
      if int(user.driver_license) == driver_license:
        self.logged_in_user = user
        self.loggedIn = True
        self.all_users = Interface.get_all_users_from_db()
        self.all_posts = Post.get_all_posts()
        return self.authenticated_menu()
    print('User not found. Try again.\n')
    return self.login()

  def add_user(self):
    print("** Enter New User Information Below **")
    tier = input('Would you like to sign up for a Free account or Premium account? (f or p)')
    name = input('Enter user name: ')
    email = input("Enter user's email: ")
    drivers_license = int(input("Enter user's driver's license: "))
    all_users = Interface.get_all_users_from_db()
    for user in all_users:
      if user.driver_license == drivers_license:
        print("A user already exists with that driver's license. Try again.")
        return self.add_user()
    if tier[0].lower() == 'f':
      all_users.append(FreeUser(name, email, drivers_license))
    elif tier[0].lower() == 'p':
      all_users.append(PremiumUser(name, email, drivers_license))
    print("""
     New User Created!
    """)
    self.save_users(all_users)

  def add_post(self):
    if self.logged_in_user.tier == 'f' and self.post_count() >= 2:
        print("You've reached the maximium amount of posts. Please upgrade to a Premium Account to make more posts.")
    else:
      print("** Enter New Post Information Below **")
      title = input('Enter Post Title: ')
      body = input("Enter Post Body: ")
      self.all_posts.append(Post(self.logged_in_user.driver_license, title, body))
      self.save_posts()

  def save_users(self, all_users):
    with open(user_path, 'w') as csvfile:
      user_csv = csv.writer(csvfile, delimiter=',')
      user_csv.writerow(['name', 'email_address', 'driver_license', 'tier'])
      for user in all_users:
        user_csv.writerow([user.name, user.email_address, user.driver_license, user.tier])

  def save_posts(self):
    with open(post_path, 'w') as csvfile:
      post_csv = csv.writer(csvfile, delimiter=',')
      post_csv.writerow(['user_id', 'title', 'body'])
      for post in self.all_posts:
        post_csv.writerow([post.user_id, post.title, post.body])

  def view_users(self):
    for user in self.all_users:
      print(user)

  def view_all_posts(self):
    for post in self.all_posts:
      print(post)

  def view_users_posts(self):
    for post in self.all_posts:
      if post.user_id == self.logged_in_user.driver_license:
        print(post)

  def post_count(self):
    num_posts = 0
    for post in self.all_posts:
      if post.user_id == self.logged_in_user.driver_license:
        num_posts += 1
    return num_posts

  @classmethod
  def get_all_users_from_db(cls):
    with open(user_path, 'r') as users_file:
      users = csv.DictReader(users_file)
      users_list = []
      for user in users:
        if user['tier'] == 'p':
          premium_user = PremiumUser(user['name'], user['email_address'], user['driver_license'])
          users_list.append(premium_user)
        else:
          free_user = FreeUser(user['name'], user['email_address'], user['driver_license'])
          users_list.append(free_user)
      return users_list


