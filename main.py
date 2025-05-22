# Drink ordering BOT
# BOT that takes customer orders for boba shop
# Programmer: Ean Siao
# Known bugs: none

# Import libraries
import random
import re
# Import pandas library
import time
import os
import sys
import pandas as pd
# Import colorama to create coloured text
from colorama import Fore, Style, init

# Constants for low and high number for menus
LOW = 1
HIGH = 2
# Constant for cost of the delivery
DELV_COST = 14

# list of names used by BOT
bot_names = ("Madge", "Abigail", "Aaron", "Eli", "Wiley", "Marie",
             "Jamaal", "Grover", "Fredrick", "Barton")

# Colours for the different categories of drinks on the menu
category_colors = {
    "Milk Tea": Fore.BLUE,
    "Tea": Fore.GREEN,
    "Slushy": Fore.YELLOW,
}

# List of dictionaries containing drink category, name and price for menu
menu_data = [
    # Milk Tea
    {"Category": "Milk Tea", "Drink": "Original Milk Tea", "Price": 8.00},
    {"Category": "Milk Tea", "Drink": "Strawberry Milk Tea", "Price": 8.00},
    {"Category": "Milk Tea", "Drink": "Chocolate Milk Tea", "Price": 8.00},
    {"Category": "Milk Tea", "Drink": "Coffee Milk Tea", "Price": 8.00},
    {"Category": "Milk Tea", "Drink": "Mocha Milk Tea", "Price": 8.00},
    {"Category": "Milk Tea", "Drink": "Taro Milk Tea", "Price": 8.20},
    {"Category": "Milk Tea", "Drink": "Caramel Milk Tea", "Price": 8.20},
    {"Category": "Milk Tea", "Drink": "Matcha Milk Tea", "Price": 8.60},
    {"Category": "Milk Tea", "Drink": "Brown Sugar Milk Tea", "Price": 10.50},

    # Tea
    {"Category": "Tea", "Drink": "Black Tea", "Price": 7.20},
    {"Category": "Tea", "Drink": "Jasmine Green Tea", "Price": 7.20},
    {"Category": "Tea", "Drink": "Peach Tea", "Price": 7.90},
    {"Category": "Tea", "Drink": "Passion Fruit Tea", "Price": 7.90},
    {"Category": "Tea", "Drink": "Mango Tea", "Price": 7.90},

    # Slushy
    {"Category": "Slushy", "Drink": "Grape Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Lemon Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Lime Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Strawberry Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Mango Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Peach Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Passion Fruit Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Kiwifruit Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Green Apple Slushy", "Price": 9.20},
    {"Category": "Slushy", "Drink": "Pineapple Slushy", "Price": 9.20},
]

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
    while True:  # Sets up while loop
        try:
            # Asks for input and tries to convert to integer
            num = int(input(question))
            if low <= num <= high:  # If input is within the specified range
                return num  # Returns valid input
            # Error message if input is out of range
            print(f"Input must be between {low} and {high}")
        except ValueError:  # If input is not an integer
            # Prints error message and restarts loop
            print("That is not a valid number")


# Validates inputs to check if they are alphabetical
# Takes question as a parameter
# Returns response if valid
def validate_alpha(question):
    while True:  # Sets up while loop
        response = input(question)  # Asks for input (string)
        # Sends input to blank remover function
        no_blanks = blank_remover(response)
        if not no_blanks.isalpha():  # Checks that input is alphabetic
            # Prints error message if not valid
            print("Input must only contain letters")
        else:  # If input is valid
            return response  # Returns input


# Removes blank spaces from response
# Takes response as a parameter
# Returns response with all whitespace removed
def blank_remover(response):
    # Replaces all whitespace with nothing
    no_blanks = re.sub(r"\s+", "", response)
    return no_blanks  # Returns cleaned response


# Welcomes the user to the Bubble Bar
# Picks a random name from bot_names list and greets the user
def welcome():
    # Selects a random name from bot_names list
    name = (random.choice(bot_names))
    # Prints welcome message with chosen name
    print("***Welcome to Bubble Bar***")
    print(f"*** My name is {name} ***")
    print("***I will be assisting you today in ordering your drinks***")


# Function allowing users to choose either click and collect or delivery
# Input request sent to integer validation function for validation
# Valid input is returned and sent to if statements for appropriate action
def pickup_delivery():
    del_pick = ""  # Creates variable to store user choice
    print("Do you want click and collect or delivery?")
    question = (f"please enter {LOW} or {HIGH}: ")
    print("Enter 1 for click and collect")
    print("Enter 2 for delivery")
    print("There is a $14 delivery fee if you choose delivery and the cost of your order is under $50")

    # Validates and stores user choice
    del_pick = integer_validation(LOW, HIGH, question)
    time.sleep(2)  # Waits 2 seconds before continuing
    print()

    if del_pick == 1:  # If user selects click and collect
        click_collect()  # Calls click and collect function

    elif del_pick == 2:  # If user selects delivery
        click_collect()  # Calls click and collect function
        delivery_info()  # Then calls delivery info function

    return del_pick  # Returns the user's delivery/pickup choice


# Function collects customer name and validates phone number
def click_collect():
    # Regular expression pattern for phone validation (8 to 10 digits)
    pattern = r"^\d{8,10}$"

    question = "Please enter your name: "  # Question for name input
    # Sends input to alpha validator function
    response = validate_alpha(question)
    # Stores response in dictionary in title class
    customer_details["name"] = response.title()

    while True:  # Sets up while loop for phone number validation
        # Question for phone input
        question = ("Please enter your phone number: ")
        response = input(question)  # Asks for input (string)
        # Sends input to blank remover function
        no_blanks = blank_remover(response)

        if re.match(pattern, no_blanks):  # Checks if input matches phone number pattern
            # Stores response in dictionary
            customer_details["phone"] = response
            break  # Exits loop
        # Prints error message for invalid input
        print("This is an invalid phone number")


# Function collects and validates delivery address details
def delivery_info():
    # Pattern checks if input starts with a digit (valid house/apartment number)
    pattern = r'^\d.*[a-zA-Z0-9]*$'

    while True:  # Sets up while loop for house number validation
        # Question for house/apartment number input
        question = "Please enter your house or apartment number: "
        response = input(question)  # Asks for input (string)
        # Sends input to blank remover function
        no_blanks = blank_remover(response)
        if re.match(pattern, no_blanks):  # Checks if input matches pattern
            # Stores response in dictionary in title class
            customer_details["house"] = response.title()
            break  # Exits loop
        # Prints error message for invalid input
        print("This is an invalid house number")

    question = "Please enter your street name: "  # Question for street name input
    # Sends input to alpha validator function
    response = validate_alpha(question)
    # Stores response in dictionary in title class
    customer_details["street"] = response.title()

    question = "Please enter your suburb name: "  # Question for suburb name input
    # Sends input to alpha validator function
    response = validate_alpha(question)
    # Stores response in dictionary in title class
    customer_details["suburb"] = response.title()


# Function displays the drink menu and processes customer orders
# Takes del_pick as parameter to determine click and collect or delivery
def menu(del_pick):
    menu_df = pd.DataFrame(menu_data)  # Creates DataFrame from menu_data list
    # Sorts menu items by category
    menu_df = menu_df.sort_values(by="Category")
    menu_df = menu_df.reset_index(drop=True)  # Resets index
    # Adds numbering column
    menu_df.insert(0, "Number", range(1, len(menu_df) + 1))

    # Displays menu grouped by category
    for category, group in menu_df.groupby("Category"):
        color = category_colors.get(
            category, Fore.WHITE)  # Gets category color
        # Prints category heading
        print(f"\n{color}=== {category} ==={Style.RESET_ALL}")
        for _, row in group.iterrows():  # Loops through each row in the group
            # {:2d} -> format as an integer and use 2 spaces
            # {:<22} -> format as left aligned in a 22 character wide space
            # {:>6} -> format as right aligned using 6 spaces and display 2 decimal places as a float
            # Prints formatted menu item details
            print(
                f"{row['Number']:2d}. {row['Drink']:<22} ${row['Price']:>6.2f}")

    # Function to process customer orders
    def cust_order():
        order = []  # Initializes empty order list

        while True:  # Sets up while loop for ordering
            # Asks for item number
            response = input(
                "\nEnter the number of the item you want to order (or 0 to finish ordering)\n")

            if not response.isdigit():  # Checks if input is a number
                # Prints error message if not
                print("Please enter a valid number")
                continue

            response = int(response)  # Converts input to integer

            if response == 0:  # Exits loop if input is 0
                break

            # Checks if number is valid in menu
            if response in menu_df["Number"].values:
                # Retrieves item from menu
                item = menu_df.loc[menu_df["Number"] == response].iloc[0]
                order.append(item)  # Adds item to order list
                print(Style.BRIGHT + f"Added {item['Drink']} to your order!")
            else:
                # Prints error for invalid item number
                print("Invalid choice, please try again.")

        time.sleep(2)  # Waits 2 seconds before continuing
        print()

        if order:  # If the order list is not empty
            print(Fore.GREEN + "Customer Details")
            # To account for different data collected for click and collect or delivery
            if del_pick == 1:  # If click and collect
                print("Click and Collect")
                print(
                    f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}")
            else:  # If delivery
                print("Delivery")
                print(
                    f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
            print()

            print(Fore.GREEN + "Order Details")
            total = 0  # Initializes total cost
            for idx, item in enumerate(order, 1):  # Loops through ordered items
                # Prints item in order
                print(Style.BRIGHT +
                      f"{idx}. {item['Drink']} - ${item['Price']:.2f}")
                total += item['Price']  # Adds item price to total

            if total < 50 and del_pick == 2:  # Adds delivery fee if order is under $50 and is delivery

                total = total + DELV_COST
                print(Style.BRIGHT +
                      '$14 delivery charge as cost of order is under $50')
            elif total > 50 and del_pick == 2:  # No charge if cost is over $50
                print(Style.BRIGHT + 'No delivery charge as cost of order is over $50')
            print()

            # Prints total cost
            print(Style.BRIGHT + f"Total Cost: ${total:.2f}")

        else:  # If order list is empty (customer doesn't order anything)
            print("You didn't order anything...")
            print("Please choose something from the menu to order")
            cust_order()  # Restarts order process

    cust_order()  # Calls customer order function


# Function to confirm if customer wants to continue or cancel their order
def continue_or_cancel():
    del_pick = ""
    print("Do you want continue with the order?")
    question = (f"please enter {LOW} or {HIGH}: ")  # Question for input
    print("Enter 1 to continue")
    print("Enter 2 to cancel")
    # Validates and stores user choice
    del_pick = integer_validation(LOW, HIGH, question)
    time.sleep(1)  # Waits 1 seconds before continuing
    print()

    if del_pick == 1:  # If user chooses to continue
        print("Thank you for your order")
        print("Your order has been sent to the kitchen")
        print("You will receive a text when it is ready for pickup or out for delivery")

    elif del_pick == 2:  # If user chooses to cancel
        print("Your order has been canceled")


# Function to prompt customer to start a new order or exit the program
def new_or_exit():
    del_pick = ""
    print("Do you want start a new order or exit program")
    question = (f"please enter {LOW} or {HIGH}: ")  # Question for input
    print("Enter 1 for new order")
    print("Enter 2 to exit")
    # Validates and stores user choice
    del_pick = integer_validation(LOW, HIGH, question)

    if del_pick == 1:  # If user chooses new order
        print("New Order")
        order_list.clear()  # Clear previous order items
        order_cost.clear()  # Clear previous order costs
        time.sleep(2)  # Waits 2 seconds before continuing
        # Clear terminal screen (cls for windows, clear for others)
        os.system('cls' if os.name == 'nt' else 'clear')
        main()  # Call main program function to start again

    elif del_pick == 2:  # If user chooses to exit
        print("Thank you for using boba BOT")
        order_list.clear()  # Clear previous order items
        order_cost.clear()  # Clear previous order costs
        sys.exit()  # Exit the program


# Function that combines other functions into program
def main():
    welcome()  # Calls welcome function
    time.sleep(2)  # Waits 2 seconds before continuing
    print()  # Extra line for formatting
    del_pick = pickup_delivery()  # Calls pickup or delivery function and stores input
    time.sleep(2)  # Waits 2 seconds before continuing
    menu(del_pick)  # Calls menu function with del_pick as an argument
    time.sleep(2)  # Waits 2 seconds before continuing
    print()  # Extra line for formatting
    continue_or_cancel()  # Calls continue or cancel function
    time.sleep(2)  # Waits 2 seconds before continuing
    print()  # Extra line for formatting
    new_or_exit()  # Calls new or exit function


main()  # Calls main function
