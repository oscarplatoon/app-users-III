from .user import User

class FreeUser(User):
    def __init__(self, name, email, drivers_license):
        super().__init__(name, email, drivers_license)

    def set_post(self, user_post):
        if len(self.user_posts) < 2:
            self.post_count += 1
            return super().set_post(user_post)
        raise ValueError("Free users are only allowed two posts. You have exceeded your free posts.")


