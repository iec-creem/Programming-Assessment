# Import pandas library 
import pandas as pd

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