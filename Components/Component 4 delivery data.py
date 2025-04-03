import re

# Customer details dictionary
customer_details = {}

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

delivery_info()

print(customer_details)