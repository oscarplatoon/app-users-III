from users.User import User


from .User import User

class PremiumUser(User):
    def __init__(self, role, name, email, password):
        super().__init__(self, role, name, email, password)

    def add_post(self, content):
        return super().add_post(content)