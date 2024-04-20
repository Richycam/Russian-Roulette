# Russian-Roulette
# This game is for linux only and might break your OS 
The main function is responsible for running the Russian Roulette game. It prompts the user to start the game and choose a number between 1 and 6. If the chosen number matches the randomly generated number, the user loses and a fork bomb is executed. Otherwise, the user wins.

Inputs

start_game: A string input that determines whether the game should be started or not.

play: A string input representing the number chosen by the user.


Flow
The function prints a banner with the text "Russian Roulette".
It prompts the user to start the game.
If the user agrees to play, it prompts the user to choose a number.
It generates a random number between 1 and 6.
If the chosen number matches the random number, the user loses and a fork bomb is executed.
Otherwise, the user wins.
If the user doesn't want to play, it prints "smart move".
Outputs
The function doesn't return any output. It only prints messages indicating whether the user wins or loses.

# To run the game 

open a linux terminal and run with python3

make sure to be in root first 

user@linux sudo -i 

root@linux python3 russianroulette.py 



