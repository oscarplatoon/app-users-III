import csv 
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
user_info_path = os.path.join(my_path, "../data/user_info.csv")
user_post_path = os.path.join(my_path, "../data/user_post.csv")

class User:
    users = []

    def __init__(self, name, email, drivers_license):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license

    def __str__(self):
        return f"Name: {self.name}, Email Address: {self.email}, Driver's License: {self.drivers_license}"

    def add_user(self, user_data):
        # User.users.append(user_data)
        self.users.append(User(**dict(user_data)))
        with open(user_info_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["name", "email", "drivers_license"])
            writer.writeheader()
            for user in self.users:
                # writer.writerow(row)
                name=user.name
                email=user.email
                drivers_license=user.drivers_license
                writer.writerow({'name': name,'email': email, 'drivers_license': drivers_license})



    def add_post(self, post):
        user_post_list = []
        
        #  user_post_list.append(post)
        #  with open (user_post_path, 'a') as csvfile:
        #      csv_object = writer(csvfile)
        #      csv_object.writerow(users_post)
        #      csv_object.writerow(user_post_list)

        with open(user_post_path, 'a', newline='') as csv_file:
             writer = csv.writer(csv_file)
             writer.writerow(post)

    @classmethod
    def all_users(cls):
        users = []

        with open(user_info_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                print(row)
                users.append(User(row[0], row[1], row[2]))
                # users.append(User(**dict(row)))

        # print(users)
        return users

    @classmethod
    def find(self,id, accounts):
        for account in accounts:
            if account.id == str(id):
                return account
        return None

    
    def view_users(self):
        users = User.all_users()
        print (self.name)
        # for row in users:
        #     print (row[0])

    
    def get_license(self):
        return self.drivers_license 


# Vincent Brunstad, vzbrunstd@msn.com, R12345
# Tom Brunstad, Trbrunstad@msn.com, R56789