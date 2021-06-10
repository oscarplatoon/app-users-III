from User import User

class PremiumUser(User):
  def __init__(self, name, email_address, driver_license):
    super().__init__(name, email_address, driver_license)
    self.tier = 'p'

  def __str__(self):
    return f"""
    Name: {self.name}
    Email: {self.email_address}
    Tier: {self.tier}
    """
