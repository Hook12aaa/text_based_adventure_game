import unittest
from unittest.mock import patch
from assets import player, validator, npc, monster, UI, main_player, save


class test_validator(unittest.TestCase):
    def test_abc(self):
        g, b = validator.is_not_abc("asbc"), validator.is_not_abc("1234")
        self.assertFalse(g)
        self.assertTrue(b)

    def test_is_range(self):
        for i in range(1, 10, 1):
            r = validator.is_not_accepted(i, 1, 10)
            self.assertFalse(r, f"_is_not_accepted failed range check {i}")

    def test_is_not_range(self):
        for i in range(20, 60, 1):
            r = validator.is_not_accepted(i, 1, 10)
            self.assertTrue(r, "is_not_accepted failed range")

    def test_bad_user_input(self):
        for i in range(70, 300):
            r = validator.is_not_accepted(chr(i), 1, 10)
            self.assertTrue(r, "it accepted special and chr")

    def test_number(self):
        r = validator.is_not_number("a")
        self.assertTrue(r, "is_not_number vaildated a string")


class test_user_interface(unittest.TestCase):
    def test_inject_vaild_options(self):
        with patch('builtins.input', return_value='1'):
            r = UI.options("1-3", 1, 3)
            print(r)
            self.assertEqual(r, 1)

    def test_inject_ask(self):
        with patch('builtins.input', return_value='hello'):
            r = UI.ask("test")
            self.assertEqual(r, "hello")

    def test_inject_A_or_D(self):
        with patch('builtins.input', return_value='A'):
            r = UI.fight_options()
            self.assertEqual(r, 'a')


class test_npc(unittest.TestCase):
    test_npc = npc()
    test_enemy = npc()
    test_fighter = npc()

    def test_gen_stats(self):
        self.assertGreaterEqual(self.test_npc.attack, 5,
                                "attack is generatored")
        self.assertEquals(self.test_npc.health, 100, "health is generatored")
        self.assertGreaterEqual(self.test_npc.defense,
                                5, "defense is generatored")

    def test_attack_value(self):
        for i in range(100):
            try:
                self.assertLess(self.test_npc.get_attack(), 150)
            except ZeroDivisionError:
                self.fail("ZeroDivisionError on get_attack()")

    def test_pain(self):
        for i in range(100):
            try:
                self.assertLess(self.test_npc.get_pain(i), 150)
            except ZeroDivisionError:
                self.fail("ZeroDivisionError on get_pain()")

    def test_fight(self):
        self.test_enemy.health = 500000000000
        self.test_enemy.name = "Kirito"
        __, win = self.test_enemy.fight(self.test_fighter)
        if win.name == self.test_enemy.name:
            self.fail(f"fight script broken for npc")

    def test_drop_tem(self):
        possible_names = ["defense", "attack", "potion"]
        obj = self.test_npc.drop_item()
        if obj.equip not in possible_names:
            self.fail("Unable to obtain item")


class test_monster(unittest.TestCase):
    monster_stats = monster()
    monster_a = monster()
    monster_b = monster()

    def test_stats(self):
        self.assertGreaterEqual(self.monster_stats.attack, 5,
                                "attack is generatored")
        self.assertGreaterEqual(self.monster_stats.defense,
                                5, "defense is generatored")

    def test_fight(self):
        self.monster_a.health = 5000000000000
        self.monster_a.name = "Fenrir"
        __, win = self.monster_a.fight(self.monster_b)
        if win.name == self.monster_a.name:
            self.fail("fight script broken for monster")


class test_file(unittest.TestCase):

    def write_test(self):
        test_player = player("test_player", "they")
        s = save.write(test_player, "test_character")
        self.assertEqual(True, s)

    def read_test(self):
        s = save.read(player("o", "o"), "test_character")
        self.assertEqual(s.name(), "test_player")
