#Distribute an even number of wins and losses given an odd number of inputs

from collections import defaultdict

combonations = defaultdict(list)

inputs = int(input("Enter an odd number of inputs\n"))

while inputs <= 0 or inputs % 2 == 0:
    print("Invalid number, try again")
    inputs = int(input("Enter an odd number of inputs\n")) 

number_of_wins_and_losses = int((inputs - 1) / 2)

for i in range(1, inputs + 1):
    for j in range(1, number_of_wins_and_losses + 1):
        num = (i + j) % inputs

        if num == 0:
            combonations[i].append(inputs)
        else:
            combonations[i].append(num)

print(combonations.items())
