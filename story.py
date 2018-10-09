
""" 
Text color
"""

from colorama import init
from colorama import Fore, Back, Style
import time
init()


"""
This is the go out function.
"""

def out():
    x = input(Fore.GREEN + Style.DIM + "Would you rather hang out with friends or buy food? (Type friends or food.) ")
    if (x == "hang out with friends" or x == "hang out" or x == "hang" or x == "out" or x == "friends"):
        print(Fore.GREEN + Style.DIM + "You decided to hang out with your friends. You and your friends order an extra large meal and split it. ")
        time.sleep(1)
        print(Fore.RED + Style.DIM + "You and you friends have a great time! ")
    elif (x == "Buy food" or x =="buy" or x == "food" or x== "buy food"):
        print(Fore.GREEN + Style.DIM + "You will go out for food alone but you will still be happy because you had food. ")
        time.sleep(1)
        print(Fore.RED + Style.DIM + "You are satisfied but you feel alone and left out.")
    else:
        print(Fore.GREEN + Style.DIM + "Sorry what was that?")
        out()
    
"""
This is the stay home function.
"""

def home():
    y = input(Fore.GREEN + Style.DIM + "Would you rather watch netflix or go online shopping? (Type netflix or shop) ")
    if (y == "netflix" or y == "watch netflix" or y == "watch"):
        print(Fore.GREEN + Style.DIM + "You binge watch your favorite show for ten hours! ")
        time.sleep(1)
        print(Fore.RED + Style.DIM + "You feel satisfied and you are happy that you are not broke. ")
    elif (y == "shopping" or y == "shop" or y == "go online shopping" or y == "go online" or y == "shop online"):
        print(Fore.GREEN + Style.DIM + "You splurge on buying new clothes and shoes. You spend so much that you were given free shipping. ")
        time.sleep(1)
        print(Fore.RED + Style.DIM + "You are now broke but at the same time, you feel boujee. ")
    else:
        print(Fore.GREEN + Style.DIM + "Sorry what was that?")
        home()


"""
Would you rather go out or stay home function
"""

def start():
    z = input(Fore.GREEN + Style.DIM + "What would you rather do, go out or stay home? ")
    if (z == "stay home" or z == "Stay home" or z == "Stay Home" or z == "stay Home" or z == "home" or z == "Home"):
        print(Fore.GREEN + Style.DIM + "When you stay home you will feel bored so you think of things to do. ")
        time.sleep(1)
        print(Fore.GREEN + Style.DIM + "The only thing you can think of doing is to watch netflix or shop online. ")
        home()
    elif (z == "go out" or z == "Go Out" or z == "go Out" or z == "Go Out" or z == "go" or z == "out" or z == "Go" or z == "Out"):
        print(Fore.GREEN + Style.DIM + "You call up your friends to ask them if they are busy this weekend.")
        time.sleep(1)
        print(Fore.GREEN + Style.DIM + "Your friends are free this weekend, you ponder if you want to go out with your friends or go get lunch yourself. ")
        out()
    else:
        print(Fore.GREEN + Style.DIM + "Sorry what was that?")
        start()
        
        
"""
Start here
"""

print(Fore.GREEN + Style.DIM + "Hello what is your name?")
name = input()
print(Fore.GREEN + Style.DIM + "Hello " + name + ", today we are going to outline how your weekend will go. ")
start()