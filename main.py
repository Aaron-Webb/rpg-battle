from classes.person import Person

# create 3 pla
player1 = Person("Cloud", 100, 90, 25, 60,)
player2 = Person("Zidane", 100, 90, 25, 60)
player3 = Person("Squall", 100, 90, 25, 60)

enemy1 = Person("Sephiroth", 100, 90, 25, 60)
enemy2 = Person("Ultimecia", 100, 90, 25, 60)
enemy3 = Person("Aeon", 100, 90, 25, 60)

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

game_on = True

while game_on == True:

    for player in players:
        player_choice = input("Please choose an action: ")
        index = int(player_choice) - 1

        # index 0 ("Attack") is a generic attack that gives damage
        if index == 0:
            # player gives damage to enemy
            damage = player.give_damage()
            enemy = player.choose_enemy(enemies)
            # enemy takes damage from player
            enemies[enemy].take_damage(damage)
            # inform player how much damage has been deal and the enemies current hp
            print("You attacked " + enemies[enemy].name + " for " + str(damage) + " damage points")
            print(enemies[enemy].name + " has " + str(enemies[enemy].hp) + " hp left.")


        
        elif index == 1:
            pass

        
        elif index == 2:
            pass

        


