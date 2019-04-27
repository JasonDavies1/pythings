import sys
from collections import defaultdict

inputs = sys.argv[1::]

number_of_inputs = len(inputs)

if number_of_inputs == 1 : 
    print("Please use more than one argument")
elif number_of_inputs % 2 == 0 :
    print("Invalid number of inputs, retry with an odd number")

wins_and_losses = int((number_of_inputs + 1) / 2)
combonations = defaultdict(list)

for index, item in enumerate(inputs) : 
    for j in range(1, wins_and_losses) : 
        combonations[inputs[index]].append(inputs[(index + j) % number_of_inputs])

for key, value in combonations.items() :
    print(key + " beats:")
    for item in value :
        print(item + " ")
    print()

player_one_name = input("What is Player 1's name?: ")
player_two_name = input("What is Player 2's name?: ") 

player_one_choice = input("Make your choice " + player_one_name + ": ") 
while player_one_choice not in inputs :
    print("Get it together " + player_one_name + " and choose something in the list!")
    player_one_choice = input("Make your choice " + player_one_name + ": ") 

player_two_choice = input("Make your choice " + player_two_name + ": ") 
while player_two_choice not in inputs : 
    print("Get it together " + player_two_name + " and choose something in the list!")
    player_two_choice = input("Make your choice " + player_two_name + ": ") 
