from  modules.User import User

class FreeUser(User):
    max_posts = 2

    def __init__(self, name, email, drivers_license):
        super().__init__(name, email, drivers_license)
        self.num_posts = 0

    def set_post(self, user_post):
        if self.num_posts < FreeUser.max_posts:
            self.user_posts.append(user_post)
            self.num_posts += 1
        else:
            raise Exception("Unable to post, maximum number of posts reached.")