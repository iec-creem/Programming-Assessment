# Constant variables for low and high number for menus 
LOW = 1
HIGH = 2

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

# Function allowing users to choose either click and collect or delivery
# Input request sent to integer validation function for validation
# Valid input is returned and sent to if statements for appropriate action
def pickup_delivery():
    del_pick = ""
    print("Do you want click and collect or delivery?")
    question = (f"please enter {LOW} or {HIGH}: ")
    print("Enter 1 for click and collect")
    print("Enter 2 for delivery")
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("Click and collect")
    elif del_pick == 2:
        print("Delivery")

pickup_delivery()