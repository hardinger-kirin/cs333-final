# Kirin Hardinger
# CS 333 Final Project
# Spring 2023

# Mini Pokémon battle simulator - players are restricted to 3 Pokémon per team
# Battle runs until an opponent has fainted each Pokémon

import os
import trainer
import pokemon
import move

def intro():
    print("                                      ,\'\\")
    print("    _.----.        ____         ,\'  _\\   ___    ___     ____")
    print("_,-\'       `.     |    |  /\`.   \\,-\'    |   \  /   |   |    \\  |`.")
    print("\\      __    \\    \'-.  | /   `.  ___    |    \\/    |   \'-.   \\ |  |")
    print(" \\.    \\ \   |  __  |  |/    ,\',\'_  `.  |          | __  |    \\|  |")
    print("   \\    \\/   /,\' _`.|      ,\' / / / /   |          ,\' _`.|     |  |")
    print("    \\     ,-\'/  /   \\    ,\'   | \\/ / ,`.|         /  /   \\  |     |")
    print("     \\    \\ |   \\_/  |   `-.  \\    `\'  /|  |    ||   \\_/  | |\    |")
    print("      \\    \\ \      /       `-.`.___,-\' |  |\\  /| \\      /  | |   |")
    print("       \\    \\ `.__,\'|  |`-._    `|      |__| \\/ |  `.__,\'|  | |   |")
    print("        \\_.-\'       |__|    `-._ |             ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Press enter to begin.")

    # only move on if "enter" is pressed
    while True:
        inp = input()
        if(not inp):
            break
    
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the amazing world of Pokémon!")

def choose_team(player):
    print("\nChoose a starter team!")
    print("*~*~*~*~*~*~*~*~*~*~*~*~")
    
    # default teams
    fire_team = [
    pokemon.Pokemon("","Charmander",39, \
        [move.Move("Scratch", 4, 100), move.Move("Dragon Breath", 6, 92), \
        move.Move("Fire Fang", 6.5, 90)]),
    pokemon.Pokemon("","Scorbunny", 50, \
        [move.Move("Tackle", 4, 100), move.Move("Flame Charge", 5, 95), \
        move.Move("Bounce", 8.5, 80)]),
    pokemon.Pokemon("","Litten", 45, \
        [move.Move("Ember", 4, 100), move.Move("Bite", 6, 91), \
        move.Move("Flamethrower", 9, 75)])
    ]

    grass_team = [
    pokemon.Pokemon("","Bulbasaur",45, \
        [move.Move("Vine Whip", 4.5, 100), move.Move("Razor Leaf", 5.5, 93), \
        move.Move("Seed Bomb", 8, 85)]),
    pokemon.Pokemon("","Rowlet", 68, \
        [move.Move("Leafage", 4, 100), move.Move("Pluck", 6, 91), \
        move.Move("Sucker Punch", 7, 88)]),
    pokemon.Pokemon("","Chikorita", 45, \
        [move.Move("Tackle", 4, 100), move.Move("Magical Leaf", 6, 92), \
        move.Move("Body Slam", 8.5, 80)])
    ]

    water_team = [
    pokemon.Pokemon("","Squirtle",44, \
        [move.Move("Water Gun", 4, 100), move.Move("Bite", 6, 91), \
        move.Move("Aqua Tail", 9, 75)]),
    pokemon.Pokemon("","Oshawott", 55, \
        [move.Move("Aqua Jet", 4, 100), move.Move("Water Pulse", 6, 91), \
        move.Move("Aqua Tail", 8.5, 80)]),
    pokemon.Pokemon("","Mudkip", 50, \
        [move.Move("Rock Smash", 4, 100), move.Move("Water Pulse", 6, 91), \
        move.Move("Surf", 9, 75)])
    ]

    print("Fire team!!! [1]\n\tCharmander, Scorbunny, and Litten\n\t"
          "Sure to get you fired up!")
    print("Grass team!!! [2]\n\tBulbasaur, Rowlet, and Chikorita\n\t"
          "Become one with nature!")
    print("Water team!!! [3]\n\tSquirtle, Oshawott, and Mudkip\n\tRefreshing!")

    # choose team
    team_choice = ""
    while (team_choice != '1') and (team_choice != '2') and (team_choice != '3'):
        team_choice = input("Who will you choose? ")
        
    if team_choice == '1':
        player.set_team(fire_team)
        print("You have chosen the fire team!")
    elif team_choice == '2':
        player.set_team(grass_team)
        print("You have chosen the grass team!")
    elif team_choice == '3':
        player.set_team(water_team)
        print("You have chosen the water team!")

def give_nicknames(player):
    nickname_choice = ""
    while nickname_choice != 'y' and nickname_choice != 'n':
        nickname_choice = input(f'{player.get_name()}, would you like to nickname \
        any of your Pokémon? [y/n] ')
    if nickname_choice == 'n':
        return

    poke_choice = ""
    while True:
        print("")
        player.list_team()
        print("")
        poke_choice = input("Enter the species of the Pokémon you would like to"
                            "nickname or \'e\' to stop nicknaming: ")
        if poke_choice == 'e':
            break

        selected_pokemon = player.find_pokemon_by_name(poke_choice)
        if selected_pokemon is not None:
            new_name = input(f'Enter a new nickname for {poke_choice}: ')
            selected_pokemon.set_nickname(new_name)
            print(f'{poke_choice} is now {selected_pokemon.get_nickname()}!')
        else:
            print("Could not find that Pokémon on your team. Please try again")

def main():
    intro()
    name = input("What is your name, young Trainer? ")
    player = trainer.Trainer(name)
    print(f'It\'s great to meet you, {player.get_name()}')
    choose_team(player)
    give_nicknames(player)

if __name__ == "__main__":
    main()