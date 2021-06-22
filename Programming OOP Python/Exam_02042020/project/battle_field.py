from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError('Player is dead!')
        if isinstance(attacker,Beginner):
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30
        if isinstance(enemy, Beginner):
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        attacker.health += sum([c.health_points for c in attacker.card_repository.cards])
        enemy.health += sum([c.health_points for c in enemy.card_repository.cards])

        # self.attack(attacker, enemy)
        # self.attack(enemy, attacker)
        # for card in att.card_repository.cards:
        #     en.take_damage(card.damage_points)

