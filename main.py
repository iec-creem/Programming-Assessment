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
import time
import os
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

boba_names = ['Original Milk Tea', 'Strawberry Milk Tea', 'Chocolate Milk Tea', 'Coffee Milk Tea', 'Mocha Milk Tea','Taro Milk Tea', 
                'Caramel Milk Tea', 'Matcha Milk Tea','Brown Sugar Milk Tea',  
                'Black Tea', 'Jasmine Green Tea', 'Peach Tea', 'Passion Fruit Tea', 'Mango Tea', 
                'Grape Slushy', 'Lemon Slushy', 'Lime Slushy', 'Strawberry Slushy', 'Mango Slushy', 'Peach Slushy', 'Passion Fruit Slushy', 
                'Kiwifruit Slushy', 'Green Apple Slushy', 'Pineapple Slushy']

boba_prices = [8.00, 8.00, 8.00, 8.00, 8.00, 8.20, 8.20, 8.60, 10.50, 7.20, 7.20, 7.90, 7.90, 7.90, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20]

# List to store ordered boba
order_list = []

# List to store boba prices
order_cost = []

# Customer details dictionary
customer_details = {}

# Set autoreset to true so that coloured text automatically stops at end of print statement
init(autoreset=True)


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


def validate_alpha(question):
    # While loop for validation of street name
    while True:
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
            return response


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
    print("There is a $14 delivery fee if you choose delivery and the cost of your order is under $50")
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        click_collect()
    elif del_pick == 2:
        click_collect()
        delivery_info()
    return del_pick


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


def delivery_info():
    # While loop for validation of house number
    while True:
        question = "Please enter your house or apartment number: "
        response = input(question)
        if response == "":
            print ("Can not be left blank")
        else:
            # Removes blank spaces from response
            no_blanks = re.sub(r"\s+", "", response)
            customer_details["house"] = response.title()
            break

    question = "Please enter your street name: "
    response = validate_alpha(question)
    # If alpha covert to title and append to dictionary
    customer_details["street"] = response.title()

    # While loop for validation of suburb
    question = "Please enter your suburb name: "
    response = validate_alpha(question)
    # If alpha covert to title and append to dictionary
    customer_details["suburb"] = response.title()


def menu():
    # Create menu dictionary
    menu_dict = {}

    # Format pizza prices as currency
    pd.options.display.float_format = '${:,.2f}'.format

    # Add pizza numbers to dictionary
    menu_dict ['Number'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

    menu_dict ['Boba Names'] = ['Original Milk Tea', 'Strawberry Milk Tea', 'Chocolate Milk Tea', 'Coffee Milk Tea', 'Mocha Milk Tea','Taro Milk Tea', 
                'Caramel Milk Tea', 'Matcha Milk Tea','Brown Sugar Milk Tea',  
                'Black Tea', 'Jasmine Green Tea', 'Peach Tea', 'Passion Fruit Tea', 'Mango Tea', 
                'Grape Slushy', 'Lemon Slushy', 'Lime Slushy', 'Strawberry Slushy', 'Mango Slushy', 'Peach Slushy', 'Passion Fruit Slushy', 
                'Kiwifruit Slushy', 'Green Apple Slushy', 'Pineapple Slushy']

    menu_dict ['Boba Prices'] = [8.00, 8.00, 8.00, 8.00, 8.00, 8.20, 8.20, 8.60, 10.50, 7.20, 7.20, 7.90, 7.90, 7.90, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20]

    # Display menu dataframe
    df =pd.DataFrame(menu_dict)
    blankIndex = [''] * len(df)
    df.index = blankIndex

    print()
    print("Boba Menu: Please order using the menu items number")
    print("Reminder: There is a $14 delivery fee if you chose delivery previously and the cost of your order is under $50 \n\n" ,df)
    print()


def cust_order():
    # Choose boba from the menu
    num_boba = 0
    print("There is a maximum of 20 drinks per order")
    while True:
        try:
            num_boba = int(input("How many drinks do you want to order? "))
            if num_boba >= 1 and num_boba <= 20:
                break
            else:
                print("Your order must be between 1 and 20")

        except ValueError:
            print("This is not a valid number")
    print(num_boba)

    # Choose pizzas from the menu
    print("Please choose drink(s) from the menu")
    for item in range(num_boba):
        while num_boba > 0:
            while True:
                try:
                    boba_ordered = int(input())
                    if boba_ordered >= 1 and boba_ordered <= 24:
                        break
                    else:
                        print("Your drink order must be between 1 and 24")
                except ValueError:
                    print("That is not a valid number")
            boba_ordered = boba_ordered-1
            order_list.append(boba_names[boba_ordered])
            order_cost.append(boba_prices[boba_ordered])
            print("{} ${:.2f}".format(boba_names[boba_ordered], boba_prices[boba_ordered]))
            num_boba = num_boba-1


def print_order(del_pick):
    print()
    # Print customer order
    print(Fore.GREEN + "Customer Details")
    # To account for different data collected for click and collect or delivery
    if del_pick == 1:
        print("Click and Collect")
        print(f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}")
    else:
        print("Delivery")
        print(f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print(Fore.GREEN + "Order Details")
    count = 0
    for item in order_list:
        print(Style.BRIGHT + "Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    # Calculate the total cost of the order using sum
    total_cost = sum(order_cost)
    if total_cost < 50 and del_pick == 2:
        total_cost = total_cost + 14
        print(Style.BRIGHT + '$14 delivery charge as cost of order is under $50')
    elif total_cost > 50 and del_pick == 2:
        print(Style.BRIGHT + 'No delivery charge as cost of order is over $50')
    print()
    print(Style.BRIGHT + "Total Cost: ${:.2f}".format(total_cost))
    print()


def continue_or_cancel():
    del_pick = ""
    print("Do you want continue with the order?")
    question = (f"please enter {LOW} or {HIGH}: ")
    print("Enter 1 to continue")
    print("Enter 2 to cancel")
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("Thank you for your order")
        print("Your order has been sent to the kitchen")
        print("You will receive a text when it is ready for pickup or out for delivery")
    elif del_pick == 2:
        print("Your order has been canceled")


# Exit program or start a new order 
def new_or_exit():
    del_pick = ""
    print("Do you want start a new order or exit program")
    question = (f"please enter {LOW} or {HIGH}: ")
    print("Enter 1 for new order")
    print("Enter 2 to exit")
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("New Order")
        # Clear data from lists 
        order_list.clear()
        order_cost.clear()
        # Run main function
        main()
    elif del_pick == 2:
        print("Thank you for using pizza BOT")
        # Clear data from lists 
        order_list.clear()
        order_cost.clear()
        # Exit program
        exit()


def main():
    welcome()
    del_pick = pickup_delivery()
    menu()
    cust_order()
    print_order(del_pick)
    continue_or_cancel()
    new_or_exit()
main()