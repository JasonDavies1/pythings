# Rock Paper Scissors

This is the main fruit that I wanted to achieve. Rock Paper Scissors is cool, however I thought that it would be cooler to have a version of it that was extensible. 

## Usage
Note: As I annoyingly found out, this will not work correctly in a bash shell in Windows, because the getpass module is used in order to hide user inputs - obviously, or else we could just choose a winning result from the displayed dictionary (Pro-cheating tactic: keep an ear out for keystrokes...) 

For bash in windows use: 

    `winpty python play.py arg1 arg2 arg3 ... argN`

For a standard windows command prompt: 

    `pythong play.py arg1 arg1 arg2 arg3 ... argN`

# Features
+ The game will auto-reject if you attempt to run the script with no parameters.
+ The game will auto-reject if you supply an EVEN number of parameters. This would cause an invalid distribution chain of wins and losses which defeats the rock paper scissors idea. 
+ The game loops until you enter "No" in the final input.
+ The game supports any odd number of parameters. If you like Rock Paper Scissors, try Rock Paper Scissors Screwdriver Hammer Spanner Chisel 

# Things that I'd like to add at some point
+ Keeping a track of how many wins a player has had during one session
+ Allowing specific player name changes
+ Introducing a "best of" mode which will run for a specified number of iterations until a winner is found

# Things that I learned in this project
+ Basic python syntax
+ The enumerate() method on arrays to get positions of elements within a given array
+ Breaking classes into submodules and importing
+ Vim is not as difficult to use as a text editor as I thought it would be!
