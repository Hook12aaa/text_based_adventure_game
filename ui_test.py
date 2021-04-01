import unittest
from unittest.mock import patch
from assets import validator, npc, monster, UI, main_player, save_info , potions , weapon , armour

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
        for _ in range(100):
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
        self.test_enemy.health = 500000000000000000
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


class test_saving(unittest.TestCase):
    def test_write(self):
        test_player = main_player("test_player", "they")
        s = save_info.write( test_player, "test_character")
        self.assertEqual(True, s)

    def test_read(self):
        rewrite_player = main_player("o", "o")
        s = save_info.read(rewrite_player, "test_player")
        self.assertEqual(s.name, "best player")


class test_player_obj(unittest.TestCase):
    my_figter = main_player("Bob", "Female")
    boss = npc()
    test_user = main_player("test", "test_gender")
    test_equip = main_player("fred","Bob")

    def test_gen_player(self):
        self.assertEqual(self.test_user.name, "test")
        self.assertEqual(self.test_user.gender, "test_gender")

    def test_have_stats(self):
        self.assertGreaterEqual(self.test_user.attack, 5,
                                "attack is generatored")
        self.assertEquals(self.test_user.health, 200, "health is generatored")
        self.assertGreaterEqual(self.test_user.defense,
                                5, "defense is generatored")

    def test_fight(self):
        with patch('builtins.input', return_value='a'):
            self.my_figter.health = 50000000000000000
            __, win =  self.my_figter.fight(self.boss)
            if win.name == self.my_figter.name:
                self.fail(f"player fight script broken {win.name}{self.my_figter.name}")
    
    def test_equip_potions(self):
        self.test_equip.health = 50
        potion = potions()
        potion.modifer = 1.25
        self.test_equip.user_equip(potion)
        self.assertEquals(self.test_equip.health, 62)
    

    def test_equip_weapons(self):
        self.test_equip.attack = 50
        knife = weapon()
        knife.modifer = 10
        self.test_equip.user_equip(knife)
        self.assertEquals(self.test_equip.attack, 60)
    

    def test_equip_armour(self):
        self.test_equip.defense = 50
        shield = armour()
        shield.modifer = 10
        self.test_equip.user_equip(shield)
        self.assertEquals(self.test_equip.defense, 60)
    
