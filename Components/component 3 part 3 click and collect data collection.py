import re

# Customer details dictionary
customer_details = {}

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
    phone_number = input("Please enter your phone number: ")
    if re.match(pattern, phone_number):
        customer_details["phone"] = phone_number
        break
    else:
        print("This is an invalid phone number")

print(customer_details)