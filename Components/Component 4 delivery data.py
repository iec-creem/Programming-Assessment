import re

# Customer details dictionary
customer_details = {}

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


print(customer_details)