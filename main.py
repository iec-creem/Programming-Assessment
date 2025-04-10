# Drink ordering BOT
# BOT that takes customer orders for boba shop
# Programmer: Ean Siao
# Known bugs: none

# Import libraries
import random
import re
# Import pandas library 
import pandas as pd
# Import sys so that program can use exit()
import sys
# Import random integer
from random import randint
# Import colorama to create coloured text
from colorama import Fore, Back, Style, init

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