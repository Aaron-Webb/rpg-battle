import random

class Spell:

    def __init__(self, name, type, spell_damage, mp_cost):
        self.name = name
        self.type = type
        self.spell_damage = spell_damage
        self.high_spell_damage = spell_damage + 20
        self.low_spell_damage = spell_damage - 20
        self.mp_cost = mp_cost


    def give_spell_damage(self):
        ''' Generated a random value between the lowest
        spell damage value and the highest spell damage
        value taken'''
        return random.randrange(self.low_spell_damage, self.high_spell_damage)
