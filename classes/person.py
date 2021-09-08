from math import hypot
import random

class Person:

    def __init__(self, name, hp, mp, attack, defence):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_hp = mp
        self.attacklow = attack - 10
        self.attackhigh = attack + 10
        self.defence = defence
        self.actions = ["Attack", "Magic", "Items"]


# For taking damage. HP reduced by the amount of damage taken
    def take_damage(self, damage):
        ''' Takes in the damage dealt to the Person
        and deducts this value from the Persons current hp value'''
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # For generating damage. Returns random value between low attack base and high attack ceiling
    def give_damage(self):
        ''' Generates a random value between the lowest attack value and the
        highest attack valu. Returns this value. This is the damage value taken 
        in by the fucntion take_damage.'''
        return random.randrange(self.attacklow, self.attackhigh)

    # Get players current hp
    def get_hp(self):
        return self.hp

    # get players max hp
    def get_max_hp(self):
        return self.max_hp
    
    
    def choose_enemy(self, enemies):
        ''' iterates through enemies and checks the current hp.
        The player can choose who to attack. '''
        i = 1

        for enemy in enemies:
            if enemy.get_hp() != 0:
                i += 1
        choice = int(input("Choose enemy: ")) - 1
        return choice

    

