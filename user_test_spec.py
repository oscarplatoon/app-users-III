import unittest
from modules.user import User
from modules.post import Post
from modules.free_user import FreeUser

class TestUser(unittest.TestCase):
    def setUp(self):
        self.test_user = User("Test Man", "test@mail.org", "PADL123456")
    
    def test_user_str(self):
        self.assertTrue(type(self.test_user.__str__), str)

    def test_user_get_license(self):
        self.assertTrue(self.test_user.get_license(), "PADL123456")

class TestFreeUser(unittest.TestCase):
    def setUp(self):
        self.test_free_user = FreeUser("Free Test Man", "freetest@mail.org", "PADL654321")

    def test_user_inheritance(self):
        self.assertTrue(self.test_free_user.get_license(), "PADL65321")

class TestPost(unittest.TestCase):
    def setUp(self):
        self.test_post = Post("This is a test post.")
        self.expected_post = "This is a test post."

    def test_post_str(self):
        self.assertTrue(type(self.test_post.__str__), str)

    def test_post_print(self):
        self.assertTrue(self.test_post.print_post(), self.expected_post)

if __name__ == "__main__":
    unittest.main()