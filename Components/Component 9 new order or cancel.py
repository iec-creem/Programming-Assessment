LOW = 1
HIGH = 2

#function validates integers
#takes parameters of low and high numbers and question
#input must be integer between low and high parameters 
#while loop until correct input is received then returns input to original function
#value error results in error message and new input request 
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

def new_or_exit():
    del_pick = ""
    print("Do you want start a new order or exit program")
    question = (f"please enter {LOW} or {HIGH}: ")
    print("Enter 1 for new order")
    print("Enter 2 to exit")
    del_pick = integer_validation(LOW, HIGH, question)
    if del_pick == 1:
        print("New Order")
    elif del_pick == 2:
        print("Exit")

new_or_exit()