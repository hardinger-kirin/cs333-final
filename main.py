# Kirin Hardinger
# CS 333 Final Project
# Spring 2023

# Mini Pokémon battle simulator - players are restricted to 3 Pokémon per team
# Battle runs until an opponent has fainted each Pokémon

import os
import trainer
import pokemon
import move
import battle_helper

#formats text to colors
class text_colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    END = '\033[0m'

#displays a given string in a given color
def color_print(string, color):
    if color == 'r':
        color = text_colors.RED
    elif color == 'g':
        color = text_colors.GREEN
    elif color == 'y':
        color = text_colors.YELLOW
    elif color == 'b':
        color = text_colors.BLUE
    else:
        color = text_colors.WHITE
    
    print(color + string + text_colors.END)

def intro():
    color_print("                                      ,\'\\", 'y')
    color_print("    _.----.        ____         ,\'  _\\   ___    ___     ____", 'y')
    color_print("_,-\'       `.     |    |  /\`.   \\,-\'    |   \  /   |   |    \\  |`.", 'y')
    color_print("\\      __    \\    \'-.  | /   `.  ___    |    \\/    |   \'-.   \\ |  |", 'y')
    color_print(" \\.    \\ \   |  __  |  |/    ,\',\'_  `.  |          | __  |    \\|  |", 'y')
    color_print("   \\    \\/   /,\' _`.|      ,\' / / / /   |          ,\' _`.|     |  |", 'y')
    color_print("    \\     ,-\'/  /   \\    ,\'   | \\/ / ,`.|         /  /   \\  |     |", 'y')
    color_print("     \\    \\ |   \\_/  |   `-.  \\    `\'  /|  |    ||   \\_/  | |\    |", 'y')
    color_print("      \\    \\ \      /       `-.`.___,-\' |  |\\  /| \\      /  | |   |", 'y')
    color_print("       \\    \\ `.__,\'|  |`-._    `|      |__| \\/ |  `.__,\'|  | |   |", 'y')
    color_print("        \\_.-\'       |__|    `-._ |             ", 'y')
    color_print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", 'y')
    color_print("Press enter to begin.", 'g')

    # only move on if "enter" is pressed
    while True:
        inp = input()
        if(not inp):
            break
    
    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the amazing world of Pokémon!")

def choose_team(player):
    print(f'\nChoose a starter team, {player.get_name()}!')
    print("*~*~*~*~*~*~*~*~*~*~*~*~")
    
    # default teams
    fire_team = [
    pokemon.Pokemon("","Charmander", 39, \
        [move.Move("Scratch", 6, 100), move.Move("Dragon Breath", 9, 90), move.Move("Fire Fang", 9.5, 85)]),
    pokemon.Pokemon("","Scorbunny", 50, \
        [move.Move("Tackle", 6, 100), move.Move("Flame Charge", 7.5, 95), move.Move("Bounce", 12.5, 70)]),
    pokemon.Pokemon("","Litten", 45, \
        [move.Move("Ember", 6, 100), move.Move("Bite", 9, 90), move.Move("Flamethrower", 13.5, 65)])
    ]

    grass_team = [
    pokemon.Pokemon("","Bulbasaur", 45, \
        [move.Move("Vine Whip", 6.5, 98), move.Move("Razor Leaf", 8, 92), move.Move("Seed Bomb", 12.5, 70)]),
    pokemon.Pokemon("","Rowlet", 68, \
        [move.Move("Leafage", 6, 100), move.Move("Pluck", 9, 90), move.Move("Sucker Punch", 10.5, 80)]),
    pokemon.Pokemon("","Chikorita", 45, \
        [move.Move("Tackle", 6, 100), move.Move("Magical Leaf", 9, 90), move.Move("Body Slam", 12.5, 70)])
    ]

    water_team = [
    pokemon.Pokemon("","Squirtle", 44, \
        [move.Move("Water Gun", 6, 100), move.Move("Bite", 9, 90), move.Move("Aqua Tail", 13.5, 65)]),
    pokemon.Pokemon("","Oshawott", 55, \
        [move.Move("Aqua Jet", 6, 100), move.Move("Water Pulse", 9, 90), move.Move("Aqua Tail", 12.5, 70)]),
    pokemon.Pokemon("","Mudkip", 50, \
        [move.Move("Rock Smash", 6, 100), move.Move("Water Pulse", 9, 90), move.Move("Surf", 13.5, 65)])
    ]

    color_print("Fire team!!! [1]\n\tCharmander, Scorbunny, and Litten\n\tSure to get you fired up!", 'r')
    color_print("Grass team!!! [2]\n\tBulbasaur, Rowlet, and Chikorita\n\tBecome one with nature!", 'g')
    color_print("Water team!!! [3]\n\tSquirtle, Oshawott, and Mudkip\n\tRefreshing!", 'b')

    # choose team
    team_choice = ""
    while (team_choice != '1') and (team_choice != '2') and (team_choice != '3'):
        team_choice = input("Who will you choose? ")
        
    if team_choice == '1':
        player.set_team(fire_team)
        color_print("You have chosen the fire team!", 'r')
        return 'r'
    elif team_choice == '2':
        player.set_team(grass_team)
        color_print("You have chosen the grass team!", 'g')
        return 'g'
    elif team_choice == '3':
        player.set_team(water_team)
        color_print("You have chosen the water team!", 'b')
        return 'b'

def give_nicknames(player):
    nickname_choice = ""
    while nickname_choice != 'y' and nickname_choice != 'n':
        nickname_choice = input(f'{player.get_name()}, would you like to nickname any of your Pokémon? [y/n] ')
    if nickname_choice == 'n':
        return

    poke_choice = ""
    while True:
        print("")
        player.list_team()
        print("")
        poke_choice = input("Enter the species of the Pokémon you would like to nickname or \'e\' to stop nicknaming: ")
        if poke_choice == 'e':
            break

        selected_pokemon = player.find_pokemon_by_name(poke_choice)
        if selected_pokemon is not None:
            new_name = input(f'Enter a new nickname for {poke_choice}: ')
            selected_pokemon.set_nickname(new_name)
            color_print(f'~*~{poke_choice} is now {selected_pokemon.get_nickname()}!~*~', 'g')
        else:
            color_print("Could not find that Pokémon on your team. Please try again", 'r')

def battle(player1, p1_color, player2, p2_color):
    p1_mon = player1.get_ace().get_nickname()
    p2_mon = player2.get_ace().get_nickname()

    color_print(f'{player1.get_name()} sends out {p1_mon}!', p1_color)
    color_print(f'{player2.get_name()} sends out {p2_mon}!', p2_color)

    # battle loop
    while True:
        # player 1 turn
        print(f'{player1.get_name()}\'s turn!')
        color_print(f'{p1_mon} has {player1.get_ace().get_hp()} health left', p1_color)
        print(f'What will {p1_mon} do?')
        player1.get_ace().display_moves()

        move_choice = ""
        while move_choice != '0' and move_choice != '1' and move_choice != '2':
            move_choice = input("Enter the number of the move you would like to use: ")
        
        # player 1 uses move
        if player1.get_ace().attack(player2.get_ace(), player1.get_ace().get_moves()[int(move_choice)]) != 0:
            color_print(f'{p1_mon} dealt {player1.get_ace().get_moves()[int(move_choice)].get_damage()} damage!', p1_color)
        else:
            color_print(f'{p1_mon} missed!', p1_color)

        if battle_helper.check_faint(player2.get_ace()):
            print("\n---------------------------")
            color_print(f'{p2_mon} has fainted!', 'r')
            if not player2.replace_ace():
                print(f'{player2.get_name()} has no Pokémon left!')
                color_print(f'~*~{player1.get_name()} wins!~*~', p1_color)
                print("---------------------------\n")
                break
            else:
                p2_mon = player2.get_ace().get_nickname()
                color_print(f'{player2.get_name()} sends out {p2_mon}!', p2_color)
                print("---------------------------\n")

        print("")
        
        # player 2 turn
        print(f'{player2.get_name()}\'s turn!')
        color_print(f'{p2_mon} has {player2.get_ace().get_hp()} health left', p2_color)
        print(f'What will {p2_mon} do?')
        player2.get_ace().display_moves()

        move_choice = ""
        while move_choice != '0' and move_choice != '1' and move_choice != '2':
            move_choice = input("Enter the number of the move you would like to use: ")
        
        # player 2 uses move
        if player2.get_ace().attack(player1.get_ace(), player2.get_ace().get_moves()[int(move_choice)]) != 0:
            color_print(f'{p2_mon} dealt {player2.get_ace().get_moves()[int(move_choice)].get_damage()} damage!', p2_color)
        else:
            color_print(f'{p2_mon} missed!', p2_color)

        if battle_helper.check_faint(player1.get_ace()):
            print("\n---------------------------")
            color_print(f'{p1_mon} has fainted!', 'r')
            if not player1.replace_ace():
                color_print(f'{player1.get_name()} has no Pokémon left!', 'r')
                color_print(f'~*~{player2.get_name()} wins!~*~', p2_color)
                print("---------------------------\n")
                break
            else:
                p1_mon = player1.get_ace().get_nickname()
                color_print(f'{player1.get_name()} sends out {p1_mon}!', p1_color)
            print("---------------------------\n")

        print("")

def main():
    intro()

    # player one
    name1 = input("What is your name, young Trainer? (Player 1): ")
    player1 = trainer.Trainer(name1)
    p1_color = ''
    color_print(f'It\'s great to meet you, {player1.get_name()}', 'g')

    # player two
    name2 = input("And what is your friend's name? (Player 2): ")
    player2 = trainer.Trainer(name2)
    p2_color = ''
    color_print(f'Welcome, {player2.get_name()}', 'g')

    # set up teams, allow players to give nicknames
    p1_color = choose_team(player1)
    player1.set_ace(player1.get_team()[0])
    give_nicknames(player1)
    p2_color = choose_team(player2)
    player2.set_ace(player2.get_team()[0])
    give_nicknames(player2)

    # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    battle(player1, p1_color, player2, p2_color)

if __name__ == "__main__":
    main()