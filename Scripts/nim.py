#This is a simple implementation of the game Nim
#The AI is set to always win, following a strategy that makes it unbeatable as long as it
#goes first

player_turn = True
total = 12

def play(a, coins):
    global player_turn
    string = ''
    for i in range(1, coins + 1):
        string += "O"
    print('{} - there are {} coins remaining'.format(str(string), str(total)))
    player_turn = not player_turn

def get_coins():
    coins_to_remove = int(input("How many coins would you like to remove?\n"))
    while coins_to_remove < 0 or coins_to_remove > 3:
        coins_to_remove = int(input("Didn't understand that, try again between 1 and 3!\n"))
    return coins_to_remove


def userTurn():
    global total
    print("Your turn!")
    coins_to_remove = get_coins()
    total = total - coins_to_remove
    play(coins_to_remove, total)


def cpuTurn():
    global total
    coins_to_remove = total % 4
    total = total - coins_to_remove
    print('\nDr Nim removed {} coins!'.format(str(coins_to_remove), str(total)))
    play(coins_to_remove, total)


print("Welcome to Nim! Remove 1 to 3 coins at a time. Whoever takes the last coin wins")

while total > 0:
    if player_turn:
        userTurn()
    else:
        cpuTurn()

if not player_turn: 
	print("You somehow managed to beat a CPU that's unbeatable. Go you!")
else: 
	print("As expected Dr Nim wins again!")