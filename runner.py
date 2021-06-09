from users.User import User
from users.FreeUser import FreeUser
from users.PremiumUser import PremiumUser
from users.interface import Interface

free = FreeUser('user', 'Reno', 'reno@gmail.com', 'my_pass', 0)

pay = PremiumUser('user', 'Reno', 'reno@gmail.com', 'my_pass')

use = User('user', 'Reno', 'reno@gmail.com', 'my_pass', 'premium')

free.add_post('first post')
free.add_post('second post')
free.add_post('third post')