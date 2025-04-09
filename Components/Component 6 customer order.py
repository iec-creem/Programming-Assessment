# Import pandas library 
import pandas as pd

boba_names = ['Original Milk Tea', 'Strawberry Milk Tea', 'Chocolate Milk Tea', 'Coffee Milk Tea', 'Mocha Milk Tea','Taro Milk Tea', 
                'Caramel Milk Tea', 'Matcha Milk Tea','Brown Sugar Milk Tea',  
                'Black Tea', 'Jasmine Green Tea', 'Peach Tea', 'Passion Fruit Tea', 'Mango Tea', 
                'Grape Slushy', 'Lemon Slushy', 'Lime Slushy', 'Strawberry Slushy', 'Mango Slushy', 'Peach Slushy', 'Passion Fruit Slushy', 
                'Kiwifruit Slushy', 'Green Apple Slushy', 'Pineapple Slushy']

boba_prices = [8.00, 8.00, 8.00, 8.00, 8.00, 8.20, 8.20, 8.60, 10.50, 7.20, 7.20, 7.90, 7.90, 7.90, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20]

# List to store ordered boba
order_list = []

# List to store boba prices
order_cost = []

def menu():
    # Create menu dictionary
    menu_dict = {}

    # Format pizza prices as currency
    pd.options.display.float_format = '${:,.2f}'.format

    # Add pizza numbers to dictionary
    menu_dict ['Number'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

    menu_dict ['Boba Names'] = ['Original Milk Tea', 'Strawberry Milk Tea', 'Chocolate Milk Tea', 'Coffee Milk Tea', 'Mocha Milk Tea','Taro Milk Tea', 
                'Caramel Milk Tea', 'Matcha Milk Tea','Brown Sugar Milk Tea',  
                'Black Tea', 'Jasmine Green Tea', 'Peach Tea', 'Passion Fruit Tea', 'Mango Tea', 
                'Grape Slushy', 'Lemon Slushy', 'Lime Slushy', 'Strawberry Slushy', 'Mango Slushy', 'Peach Slushy', 'Passion Fruit Slushy', 
                'Kiwifruit Slushy', 'Green Apple Slushy', 'Pineapple Slushy']

    menu_dict ['Boba Prices'] = [8.00, 8.00, 8.00, 8.00, 8.00, 8.20, 8.20, 8.60, 10.50, 7.20, 7.20, 7.90, 7.90, 7.90, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20]

    # Display menu dataframe
    df =pd.DataFrame(menu_dict)
    blankIndex = [''] * len(df)
    df.index = blankIndex

    print()
    print("Pizza Menu: Please order using the menu items number \n\n" ,df)
    print()

menu()

# Choose boba from the menu
num_boba = 0
while True:
    try:
        num_boba = int(input("How many drinks do you want to order? "))
        if num_boba >= 1 and num_boba <= 20:
            break
        else:
            print("Your order must be between 1 and 20")

    except ValueError:
        print("This is not a valid number")
print(num_boba)

# Choose pizzas from the menu
print("Please choose boba from the menu")
for item in range(num_boba):
    while num_boba > 0:
        boba_ordered = int(input())
        boba_ordered = boba_ordered-1
        order_list.append(boba_names[boba_ordered])
        order_cost.append(boba_prices[boba_ordered])
        print(boba_names[boba_ordered], boba_prices[boba_ordered])
        num_boba = num_boba-1

print(order_list)
print(order_cost)