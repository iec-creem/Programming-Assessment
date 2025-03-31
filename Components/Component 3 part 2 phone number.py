import re

# Customer details dictionary
customer_details = {}

# Regular expression pattern for phone validation
pattern = r"^\d{8,10}$"

# Ask for user input
phone_number = input("Please enter your phone number: ")
if re.match(pattern, phone_number):
    customer_details["phone"] = phone_number
else:
    print("this is an invalid phone number")

print(customer_details)