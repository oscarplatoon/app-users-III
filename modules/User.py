from modules.post import Post

class User:
    def __init__(self, name, email, drivers_license):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self.user_posts = []
    
    def __str__(self):
        output = f"Name: {self.name}, Email Address: {self.email}, Driver's License: {self.drivers_license}\n"
        for post in self.user_posts:
            output += post.print_post()
            output += "\n"
        return output
    
    def get_license(self):
        return self.drivers_license
    
    def set_post(self, user_post):
        self.user_posts.append(user_post)