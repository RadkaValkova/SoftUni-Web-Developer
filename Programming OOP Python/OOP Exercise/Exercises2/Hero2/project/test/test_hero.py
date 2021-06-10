# from Exercises2.Hero2.project.project.hero import Hero
from project.hero import Hero
import unittest


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('a', 1, 10.0, 10.0)

    def test_initialization(self):
        self.assertEqual(self.hero.username, 'a')
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, 10.0)
        self.assertEqual(self.hero.damage, 10.0)

    def test_raise_exc_if_enemy_has_same_username(self):
        enemy = Hero('a', 1, 1.0, 1.0)
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy)
        self.assertEqual(str(exc.exception), 'You cannot fight yourself')

    def test_raise_exc_if_self_health_less_or_equal_to_zero(self):
        health_values = (0, -1)
        enemy = Hero('b', 1, 1.0, 1.0)
        for value in health_values:
            self.hero.health = value
            with self.assertRaises(Exception) as exc:
                self.hero.battle(enemy)
            self.assertEqual(str(exc.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_raise_exc_if_enemy_health_less_or_equal_to_zero(self):
        health_values = (0, -1)
        enemy = Hero('b', 1, 1.0, 1.0)
        for value in health_values:
            enemy.health = value
            with self.assertRaises(Exception) as exc:
                self.hero.battle(enemy)
            self.assertEqual(str(exc.exception), 'You cannot fight b. He needs to rest')

    def test_self_health_after_battle(self):
        enemy = Hero('b', 1, 10.0, 10.0)
        enemy_hero_damage = enemy.level * enemy.damage
        self.assertEqual(self.hero.health - enemy_hero_damage, 0)

    def test_enemy_health_after_battle(self):
        enemy = Hero('b', 1, 10.0, 10.0)
        player_damage = self.hero.level * self.hero.damage
        self.assertEqual(enemy.health - player_damage, 0)

    def test_draw(self):
        enemy = Hero('b', 1, 10.0, 10.0)
        self.assertEqual(self.hero.battle(enemy), 'Draw')

    def test_win(self):
        enemy = Hero('b', 1, 1.0, 1.0)
        res = (self.hero.battle (enemy))
        self.assertEqual(res, "You win")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 14)
        self.assertEqual(self.hero.damage, 15)

    def test_lose(self):
        enemy = Hero('b', 1, 100.0, 100.0)
        res = (self.hero.battle(enemy))
        self.assertEqual(res, "You lose")
        self.assertEqual(enemy.level, 2)
        self.assertEqual(enemy.health, 95)
        self.assertEqual(enemy.damage, 105)

    def test_str(self):
        res = self.hero.__str__()
        self.assertEqual(res, 'Hero a: 1 lvl\nHealth: 10.0\nDamage: 10.0\n')


if __name__ == "__main__":
    unittest.main()
