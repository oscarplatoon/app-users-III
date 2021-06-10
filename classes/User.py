import csv 
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
user_info_path = os.path.join(my_path, "../data/user_info.csv")


class User:
    users = []

    def __init__(self, name, email, drivers_license):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license

    def __str__(self):
        return f"Name: {self.name}, Email Address: {self.email}, Driver's License: {self.drivers_license}"

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

    @classmethod # for finding users, needs updaing
    def find(self,id, accounts):
        for account in accounts:
            if account.id == str(id):
                return account
        return None
    


    def add_user(self, user_data):
        self.users.append(User(**dict(user_data)))
        with open(user_info_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["name", "email", "drivers_license"])
            writer.writeheader()
            for user in self.users:
                name=user.name
                email=user.email
                drivers_license=user.drivers_license
                writer.writerow({'name': name,'email': email, 'drivers_license': drivers_license})

    def view_users(self):
        users = User.all_users()
        print (self.name)


# Vincent Brunstad, vzbrunstd@msn.com, R12345
# Tom Brunstad, Trbrunstad@msn.com, R56789