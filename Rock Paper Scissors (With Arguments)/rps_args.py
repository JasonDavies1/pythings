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
