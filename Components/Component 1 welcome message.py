#import library random
import random
#import random integer
from random import randint

#list of names used by BOT
bot_names = ("Madge", "Abigail", "Aaron", "Eli", "Wiley", "Marie",
             "Jamaal", "Grover", "Fredrick", "Barton")


def welcome():
    num = randint(0,9)
    name = (bot_names[num])
    print("***Welcome to Bubble Bar***")
    print("***My name is", name, "***")
    print("***I will be assisting you today in ordering your drinks***")

def main():
    welcome()

main()