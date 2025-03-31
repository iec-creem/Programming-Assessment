# Customer details dictionary
customer_details = {}

# While loop for validation of name
while True:
    question = "Please enter your name: "
    response = input(question)
    # Checking if input is alphabetical
    x = response.isalpha()
    if x == False:
        # If not then print error message
        print("Input must only contain letters")
    else:
        # If alpha covert to title and append to dictionary
        customer_details["name"] = response
        break

print(customer_details)