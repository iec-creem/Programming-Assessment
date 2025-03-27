print("Do you want click and collect or delivery?")
print("Enter 1 for click and collect")
print("Enter 2 for delivery")

try:
    choice = int(input("please enter 1 or 2"))
except ValueError:
    print("That is not a valid number")

if choice == 1:
    print("Click and collect")
elif choice == 2:
    print("Delivery")
else: print("Error")
