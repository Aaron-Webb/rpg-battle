import random

class Spell:

    def __init__(self, name, type, damage, mp_cost):
        self.name = name
        self.type = type
        self.damage = damage
        self.mp_cost = mp_cost


    def give_spell_damage(self):
        ''' Generated a random value between the lowest
        spell damage value and the highest spell damage
        value taken'''
        low_spell_damage = self.damage - 20
        high_spell_damage = self.damage + 20        
        return random.randrange(low_spell_damage, high_spell_damage)
