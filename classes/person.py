import random
import random

class Person:

    def __init__(self, name, hp, mp, attack, defence, magic):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.attacklow = attack - 10
        self.attackhigh = attack + 10
        self.defence = defence
        self.actions = ["Attack", "Magic", "Items"]
        self.magic = magic


# For taking damage. HP reduced by the amount of damage taken
    def take_damage(self, damage):
        ''' Takes in the damage dealt to the Person taken 
        in by the function take_damage and deducts this value 
        from the Persons current hp value'''
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # For generating damage. Returns random value between low attack base and high attack ceiling
    def give_damage(self):
        ''' Generates a random value between the lowest attack value and the
        highest attack value. Returns this value. This is the damage value .'''
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
                print(str(i) + "." + enemy.name)
                i += 1    
        choice = int(input("Choose enemy: ")) - 1        
        return choice


    def choose_action(self):
        i = 1
        print(self.name, "- It is your turn to attack")
        print("actions: " )
        for item in self.actions:
            print(str(i), item)
            i += 1

    def choose_magic(self):
        i = 1
        for spell in self.magic:
            print(str(i) + spell.name + " - cost: " + str(spell.cost))
            i += 1
