from .user import User

class PremiumUser(User):

    def __init__(self, name, email, drivers_license):
        super().__init__(name, email, drivers_license)