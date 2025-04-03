import re

# Customer details dictionary
customer_details = {}

# While loop for validation of street name
while True:
    question = "Please enter your street name: "
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
        customer_details["street"] = response.title()
        break

# While loop for validation of suburb
while True:
    question = "Please enter your suburb name: "
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
        customer_details["suburb"] = response.title()
        break

print(customer_details)