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

# Constant variables for low and high number for menus 
LOW = 1
HIGH = 2

#list of names used by BOT
bot_names = ("Madge", "Abigail", "Aaron", "Eli", "Wiley", "Marie",
             "Jamaal", "Grover", "Fredrick", "Barton")

# Customer details dictionary
customer_details = {}


# Function validates integers
# Takes parameters of low and high numbers and question
# Input must be integer between low and high parameters 
# While loop until correct input is received then returns input to original function
# Value error results in error message and new input request 
def integer_validation(low, high, question): 
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                (f"please enter {LOW} or {HIGH}: ")
        except ValueError:
            print("That is not a valid number")
            (f"please enter {LOW} or {HIGH}: ")


def welcome():
    num = randint(0,9)
    name = (bot_names[num])
    print("***Welcome to Bubble Bar***")
    print("***My name is", name, "***")
    print("***I will be assisting you today in ordering your drinks***")


# Function allowing users to choose either click and collect or delivery
# Input request sent to integer validation function for validation
# Valid input is returned and sent to if statements for appropriate action
def pickup_delivery():
    del_pick = ""
    print("Do you want click and collect or delivery?")
    question = (f"please enter {LOW} or {HIGH}: ")
    print("Enter 1 for click and collect")
    print("Enter 2 for delivery")
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        click_collect()
    elif del_pick == 2:
        print("Delivery")


def click_collect():
    # Regular expression pattern for phone validation
    pattern = r"^\d{8,10}$"

    # While loop for validation of name
    while True:
        question = "Please enter your name: "
        response = input(question)
        # Removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", response)
        # Checking if input is alphabetical
        x = no_blanks.isalpha()
        if x == False:
            # If not then print error message
            print("Input must only contain letters")
        else:
            # If alpha covert to title and append to dictionary
            customer_details["name"] = response.title()
            break

    # While loop for validation of phone number
    while True:
        # Asks for user input
        question = ("Please enter your phone number: ")
        response = input(question)
        # Removes blank spaces from response
        no_blanks = re.sub(r"\s+", "", response)
        phone_number = response
        if re.match(pattern, no_blanks):
            phone_number = no_blanks
            customer_details["phone"] = phone_number
            break
        else:
            print("This is an invalid phone number")


def main():
    welcome()
    pickup_delivery()
main()

print(customer_details)