from users.User import User
from users.Post import Post

class FreeUser():
  def check_post_amount(self):
    if self.post_amount < 2:
      print('Hit limit to post. :/')
