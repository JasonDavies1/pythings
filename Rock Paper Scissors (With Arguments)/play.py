import sys
import rps_setup as setup

inputs = sys.argv[1::]
number_of_inputs = len(inputs)

def play_again() :
    selection = input("Play Again? (Yes/No): ")
    options = ["Yes", "No"] 
    while selection not in options :
        print("Please try again...")
        selection = input("Play Again? (Yes/No): ")
    return selection

#setup
setup.check_arguments_correct(number_of_inputs)
wins_and_losses = int((number_of_inputs + 1) / 2)
combinations = setup.generate_combinations(inputs, wins_and_losses, number_of_inputs)
setup.display_wins_losses_dictionary(combinations)
player_one_name = setup.get_player_name(1)
player_two_name = setup.get_player_name(2)

replay = 'Yes'

#this should loop
while replay != 'No' : 
    player_one_choice = setup.get_player_choice(player_one_name, inputs)
    player_two_choice = setup.get_player_choice(player_two_name, inputs)

    player_one_results = combinations[player_one_choice]

    print(setup.get_result(player_one_name, player_two_name, player_one_choice, player_two_choice, player_one_results))
    replay = play_again()
