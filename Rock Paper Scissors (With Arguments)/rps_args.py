import sys
from getpass import getpass
from collections import defaultdict

inputs = sys.argv[1::]

number_of_inputs = len(inputs)

def check_arguments_correct(n) :
    if number_of_inputs == 1 : 
        print("Please use more than one argument")
        sys.exit()
    elif number_of_inputs % 2 == 0 :
        print("Invalid number of inputs, retry with an odd number")
        sys.exit()

def generateCombonations(inputs, wins_losses) :
    combonations = defaultdict(list)
    for index, item in enumerate(inputs) : 
        for j in range(1, wins_and_losses) : 
            combonations[inputs[index]].append(inputs[(index + j) % number_of_inputs])
    return combonations

def display_wins_losses_dictionary(dic) :
    for key, value in combonations.items() :
        print(key + " beats: " + ", ".join(value) + "\n")

def get_player_name(player_number) :
    return input("What is Player " + str(player_number) + "'s name?: ")

def get_player_choice(name, inputs):
    player_choice = getpass("Make your choice " + name + ": ") 
    while player_choice not in inputs :
        print("Get it together " + name + " and choose something in the list!")
        player_choice = getpass("Make your choice " + name + ": ") 
    return player_choice

def assert_winner(p1_name, p2_name, p1_choice, p2_choice, p1_results) :
    if p1_choice == p2_choice :
        print("Tie game!")
        sys.exit()
    elif p2_choice in p1_results :
        print(p1_name + " wins!")
        sys.exit()
    else :
        print(p2_name + " wins!")

#setup
check_arguments_correct(number_of_inputs)
wins_and_losses = int((number_of_inputs + 1) / 2)
combonations = generateCombonations(inputs, wins_and_losses)
display_wins_losses_dictionary(combonations)
player_one_name = get_player_name(1)
player_two_name = get_player_name(2)

#this should loop
player_one_choice = get_player_choice(player_one_name, inputs)
player_two_choice = get_player_choice(player_two_name, inputs)

player_one_results = combonations[player_one_choice]

assert_winner(player_one_name, player_two_name, player_one_choice, player_two_choice, player_one_results)
