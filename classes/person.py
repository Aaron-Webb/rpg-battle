class Person:

    def __init__(self, name, hp, mp, attack, defence, magic, items):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_hp = mp
        self.attacklow = attack - 10
        self.attachigh = attack + 10
        self.defence = defence
        self.magic = magic
        self.items = items
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
    def generate_damage(self):
        ''' Generates a random value between the lowest attack value and the
        highest attack valu. Returns this value. This is the damage value taken 
        in by the fucntion take_damage.'''
        return random.randrange(self.attacklow, self.attackhigh)