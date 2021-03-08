import unittest
from assets import validator, npc


class test_vaildator(unittest.TestCase):
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
        self.test_enemy.health = 500000
        win, __ = self.test_enemy.fight(self.test_fighter)
        if win.name == self.test_fighter.name:
            self.fail(f"fight script broken")
