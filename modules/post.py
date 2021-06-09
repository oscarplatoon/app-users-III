class Post:
    def __init__(self, user_post):
        self.user_post = user_post
    
    def __str__(self):
        return self.user_post
    
    def print_post(self):
        return self.user_post