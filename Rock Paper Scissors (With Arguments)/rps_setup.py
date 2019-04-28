import sys
from collections import defaultdict
from getpass import getpass

def check_arguments_correct(n) :
    if n == 1 : 
        print("Please use more than one argument")
        sys.exit()
    elif n % 2 == 0 :
        print("Invalid number of inputs, retry with an odd number")
        sys.exit()

def generateCombonations(inputs, wins_losses, number_of_inputs) :
    combonations = defaultdict(list)
    for index, item in enumerate(inputs) : 
        for j in range(1, wins_losses) : 
            combonations[inputs[index]].append(inputs[(index + j) % number_of_inputs])
    return combonations

def display_wins_losses_dictionary(dic) :
    for key, value in dic.items() :
        print(key + " beats: " + ", ".join(value) + "\n")

def get_player_name(player_number) :
    return input("What is Player " + str(player_number) + "'s name?: ")

def get_player_choice(name, inputs):
    player_choice = getpass("Make your choice " + name + ": ") 
    while player_choice not in inputs :
        print("Get it together " + name + " and choose something in the list!")
        player_choice = getpass("Make your choice " + name + ": ") 
    return player_choice

def get_result(p1_name, p2_name, p1_choice, p2_choice, p1_results) :
    result = ''
    if p1_choice == p2_choice :
        result = "Tie game!"
    elif p2_choice in p1_results :
        result = "{} wins!".format(p1_name)
    else :
        result = "{} wins!".format(p2_name)
    return result


