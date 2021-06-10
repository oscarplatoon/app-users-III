import csv
import os

my_path = os.path.abspath(os.path.dirname(__file__))
user_post_path = os.path.join(my_path, "../data/user_post.csv")

class Posts:

    def __init__(self, name, post):
        self.name = name
        self.post = post

    @classmethod
    def all_posts(self):
        posts = []

        with open(user_post_path) as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                print(row)
                posts.append(Posts(row[0], row[1]))
        return posts

    def add_post(self, post):
        # User.users.append(user_data)
        self.posts.append(Posts(**dict(post)))
        with open(user_post_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = ["name", "post"])
            writer.writeheader()
            for user in self.posts:
                # writer.writerow(row)
                name=user.name
                post=user.post
                writer.writerow({'name': name,'post': post})

# Vince Brunstad, Ankur really likes doughnuts
# Donna Brunstad, Vince is the best