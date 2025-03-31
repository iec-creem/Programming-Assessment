import re

# Customer details dictionary
customer_details = {}

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

print(customer_details)