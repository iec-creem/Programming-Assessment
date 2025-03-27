LOW = 1
HIGH = 2
print("Do you want click and collect or delivery?")
print("Enter 1 for click and collect")
print("Enter 2 for delivery")

while True:
    try:
        num = int(input("please enter 1 or 2"))
        if num >= LOW and num <= HIGH:
            if num == 1:
                print("Click and collect")
                break
            elif num == 2:
                print("Delivery")
                break
            else: num = int(input("Please enter 1 or 2"))
    except ValueError:
        print("That is not a valid number please only enter 1 or 2")

print("continue")