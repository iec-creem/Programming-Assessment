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
import pandas as pd
# Import colorama to create coloured text
from colorama import Fore, Style, init

# Constants for low and high number for menus
LOW = 1
HIGH = 2

DELV_COST = 14
# list of names used by BOT
bot_names = ("Madge", "Abigail", "Aaron", "Eli", "Wiley", "Marie",
             "Jamaal", "Grover", "Fredrick", "Barton")

category_colors = {
    "Milk Tea": Fore.BLUE,
    "Tea": Fore.GREEN,
    "Slushy": Fore.YELLOW,
}

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
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Input must be between {low} and {high}")
        except ValueError:
            print("That is not a valid number")


def validate_alpha(question):
    # While loop for validation of alphabetical
    while True:
        response = input(question)
        no_blanks = blank_remover(response)
        # Checking if input is alphabetical
        x = no_blanks.isalpha()
        if x is False:
            # If not then print error message
            print("Input must only contain letters")
        else:
            # If alpha covert to title and append to dictionary
            return response


def blank_remover(response):
    # Removes blank spaces from response
    no_blanks = re.sub(r"\s+", "", response)
    return no_blanks


def welcome():
    name = (random.choice(bot_names))
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
    time.sleep(2)
    print()
    if del_pick == 1:
        click_collect()
    elif del_pick == 2:
        click_collect()
        delivery_info()
    return del_pick


def click_collect():
    # Regular expression pattern for phone validation
    pattern = r"^\d{8,10}$"

    question = "Please enter your name: "
    response = validate_alpha(question)
    customer_details["name"] = response.title()

    # While loop for validation of phone number
    while True:
        # Asks for user input
        question = ("Please enter your phone number: ")
        response = input(question)
        # Removes blank spaces from response
        no_blanks = blank_remover(response)
        phone_number = response
        if re.match(pattern, no_blanks):
            phone_number = no_blanks
            customer_details["phone"] = phone_number
            break
        else:
            print("This is an invalid phone number")


def delivery_info():
    pattern = r'^\d.*[a-zA-Z0-9]*$'
    # While loop for validation of house number
    while True:
        question = "Please enter your house or apartment number: "
        response = input(question)
        no_blanks = blank_remover(response)
        if re.match(pattern, no_blanks):
            customer_details["house"] = response.title()
            break
        else:
            print("This is an invalid house number")

    question = "Please enter your street name: "
    response = validate_alpha(question)
    # If alpha covert to title and append to dictionary
    customer_details["street"] = response.title()

    # While loop for validation of suburb
    question = "Please enter your suburb name: "
    response = validate_alpha(question)
    # If alpha covert to title and append to dictionary
    customer_details["suburb"] = response.title()


def menu(del_pick):
    # Drink list display function
    # Create DataFrame
    menu_df = pd.DataFrame(menu_data)

    # Sort by category
    menu_df = menu_df.sort_values(by="Category")

    # Reset index and reassign numbering
    menu_df = menu_df.reset_index(drop=True)
    menu_df.insert(0, "Number", range(1, len(menu_df) + 1))

    # Alignment and printing
    for category, group in menu_df.groupby("Category"):
        # Default color to white
        color = category_colors.get(category, Fore.WHITE)
        print(f"\n{color}=== {category} ==={Style.RESET_ALL}")
        for _, row in group.iterrows():
            # {:2d} -> number (2 digits), {:25s} -> item name (25 characters wide, left-aligned), {:>6} -> price (right-aligned 6 spaces)
            print(
                f"{row['Number']:2d}. {row['Drink']: <22} ${row['Price']:>6.2f}")

    def cust_order():
        # Start Order
        order = []

        # Loop order while ordering
        while True:
            response = input(
                "\nEnter the number of the item you want to order (or 0 to finish ordering)\n")

            if not response.isdigit():
                print("Please enter a valid number")
                continue

            response = int(response)

            if response == 0:
                break

            if response in menu_df["Number"].values:
                item = menu_df.loc[menu_df["Number"] == response].iloc[0]
                order.append(item)
                print(Style.BRIGHT + f"Added {item['Drink']} to your order!")

            else:
                print("Invalid choice, please try again.")

        time.sleep(2)
        print()
        if order:
            # Print customer order
            print(Fore.GREEN + "Customer Details")
            # To account for different data collected for click and collect or delivery
            if del_pick == 1:
                print("Click and Collect")
                print(
                    f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}")
            else:
                print("Delivery")
                print(
                    f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
            print()
            print(Fore.GREEN + "Order Details")
            total = 0
            for idx, item in enumerate(order, 1):
                print(Style.BRIGHT +
                      f"{idx}. {item['Drink']} - ${item['Price']:.2f}")
                total += item['Price']
            if total < 50 and del_pick == 2:
                total = total + DELV_COST
                print(Style.BRIGHT +
                      '$14 delivery charge as cost of order is under $50')
            elif total > 50 and del_pick == 2:
                print(Style.BRIGHT + 'No delivery charge as cost of order is over $50')
            print()
            print(Style.BRIGHT + f"Total Cost: ${total:.2f}")

        else:
            print("You didn't order anything...")
            print("Please choose something from the menu to order")
            cust_order()  # If customer does not order anything, the cust order function is called again so that they can order items
    cust_order()


def continue_or_cancel():
    del_pick = ""
    print("Do you want continue with the order?")
    question = (f"please enter {LOW} or {HIGH}: ")
    print("Enter 1 to continue")
    print("Enter 2 to cancel")
    del_pick = integer_validation(LOW, HIGH, question)
    time.sleep(1)
    print()
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
        time.sleep(2)
        os.system('cls')
        # Run main function
        main()
    elif del_pick == 2:
        print("Thank you for using boba BOT")
        # Clear data from lists
        order_list.clear()
        order_cost.clear()
        # Exit program
        exit()


def main():
    welcome()
    time.sleep(2)
    print()
    del_pick = pickup_delivery()
    time.sleep(2)
    menu(del_pick)
    time.sleep(2)
    print()
    continue_or_cancel()
    time.sleep(2)
    print()
    new_or_exit()


main()
