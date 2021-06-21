# from Testing.hero.project.project.hero import Hero
from project.hero import Hero
import unittest


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('B', 1, 10.0, 10.0)

    def test_init(self):
        self.assertEqual(self.hero.username, 'B')
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 10.0)
        self.assertEqual(self.hero.damage, 10.0)

    def test_raise_excep_if_usn_equal_enemy_name(self):
        enemy_hero = Hero('B', 1, 10.0, 10.0)
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(exc.exception), 'You cannot fight yourself')

    def test_raise_excep_if_health_less_than_zero(self):
        enemy_hero = Hero('C', 1, 10.0, 10.0)
        self.hero.health = -2
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(exc.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_raise_excep_if_health_zero(self):
        enemy_hero = Hero('C', 1, 10.0, 10.0)
        self.hero.health = 0
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(exc.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_raise_excep_if_healt_enemy_less_than_zero(self):
        enemy_hero = Hero('C', 1, -2, 10.0)
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(exc.exception), f'You cannot fight {enemy_hero.username}. He needs to rest')

    def test_raise_excep_if_healt_enemy_zero(self):
        enemy_hero = Hero('C', 1, 0, 10.0)
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(exc.exception), f'You cannot fight {enemy_hero.username}. He needs to rest')

    def test_hero_damage(self):
        player_damage = self.hero.damage * self.hero.level
        self.assertEqual(player_damage, 10)

    def test_enemy_damage(self):
        enemy_hero = Hero('C', 1, 10.0, 10.0)
        enemy_damage = enemy_hero.damage * enemy_hero.level
        self.assertEqual(enemy_damage, 10)

    def test_hero_health_decrease(self):
        enemy_hero = Hero('C', 1, 10.0, 5.0)
        self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.health-enemy_hero.damage, 5)

    # def test_enemy_health_decrease(self):
    #     enemy_hero = Hero('C', 1, 15.0, 10.0)
    #     self.hero.battle(enemy_hero)
    #     hero_damage = self.hero.level * self.hero.damage
    #     self.assertEqual(enemy_hero.health-hero_damage, 5)

    def test_healts_below_zero(self):
        enemy_hero = Hero('C', 1, 10, 10.0)
        self.assertEqual(self.hero.battle(enemy_hero), 'Draw')

    def test_hero_winning(self):
        enemy_hero = Hero('C', 1, 1.0, 1.0)
        res = self.hero.battle(enemy_hero)
        self.assertEqual(res, 'You win')
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 14.0)
        self.assertEqual(self.hero.damage, 15.0)

    def test_hero_losing(self):
        enemy_hero = Hero('C', 100, 100.0, 10.0)
        res = self.hero.battle(enemy_hero)
        self.assertEqual(res, 'You lose')
        self.assertEqual(enemy_hero.level, 101)
        self.assertEqual(enemy_hero.health, 95.0)
        self.assertEqual(enemy_hero.damage, 15.0)

    def test_str_vehicle(self):
        self.assertEqual(self.hero.__str__(), "Hero B: 1 lvl\nHealth: 10.0\nDamage: 10.0\n")



if __name__ == '__main__':
    unittest.main()