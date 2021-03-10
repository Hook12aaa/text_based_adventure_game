from assets import main_player
import unittest


class test_player_obj(unittest.TestCase):
    my_figter = main_player("Bob", "Female")
    test_user = main_player("test", "test_gender")

    def gen_player(self):
        self.assertEqual(self.test_user.name, "test")
        self.assertEqual(self.test_user.gender, "test_gender")

    def have_stats(self):
        self.assertGreaterEqual(self.test_user.attack, 5,
                                "attack is generatored")
        self.assertEquals(self.test_user.health, 200, "health is generatored")
        self.assertGreaterEqual(self.test_user.defense,
                                5, "defense is generatored")
