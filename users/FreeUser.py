from .User import User


class FreeUser(User):
    def __init__(self, role, name, email, password, posts_count):
        super().__init__(role, name, email, password, posts_count)

    def add_post(self, content):
        if self.posts_count > 2:
            raise Exception("Upgrade tp Premium to create most posts!")
        return super().add_post(content)