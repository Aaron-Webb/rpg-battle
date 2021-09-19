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
        player.choose_action()
        player_choice = input("Please choose an action: ")
        index = int(player_choice) - 1

        # index 0 ("Attack") is a generic attack that gives damage
        if index == 0:
            # player choose the enemy
            enemy = player.choose_enemy(enemies)
            # player gives damage to enemy
            damage = player.give_damage() 
            # enemy takes damage from player
            enemies[enemy].take_damage(damage)
            # inform player how much damage has been deal and the enemies current hp
            print("You attacked " + enemies[enemy].name + " for " + str(damage) + " damage points")
            if enemies[enemy].hp == 0:
                print(enemies[enemy].name + " has died.")
                del enemies[enemy]
            else:
                print(enemies[enemy].name + " has " + str(enemies[enemy].hp) + " hp left.")


        
        elif index == 1:
            pass

        
        elif index == 2:
            pass
    

    # Game over.. who won?       
    
    killed_players = 0
    killed_enemies = 0

    for player in players:
        if player.get_hp() == 0:
            killed_players += 1
    
    for enemy in enemies:
        if enemy.get_hp() == 0:
            killed_enemies += 1
    
    if killed_enemies == 3:
        print("You win!")
        game_on = False
    elif killed_players == 3:
        print("You lose!")
        game_on = False


        


