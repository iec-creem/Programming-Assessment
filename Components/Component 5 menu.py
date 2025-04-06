boba_names = ['Original Milk Tea', 'Strawberry Milk Tea', 'Chocolate Milk Tea', 'Coffee Milk Tea', 'Mocha Milk Tea','Taro Milk Tea', 
              'Caramel Milk Tea', 'Matcha Milk Tea','Brown Sugar Milk Tea',  
               'Black Tea', 'Jasmine Green Tea', 'Peach Tea', 'Passion Fruit Tea', 'Mango Tea', 
               'Grape Slushy', 'Lemon Slushy', 'Lime Slushy', 'Strawberry Slushy', 'Mango Slushy', 'Peach Slushy', 'Passion Fruit Slushy', 
               'Kiwifruit Slushy', 'Green Apple Slushy', 'Pineapple Slushy']

boba_prices = [8.00, 8.00, 8.00, 8.00, 8.00, 8.20, 8.20, 8.60, 10.50, 7.20, 7.20, 7.90, 7.90, 7.90, 
               9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20, 9.20]

NUMBER_BOBA = 24
for count in range(NUMBER_BOBA):
    print("{} {} ${:.2f}".format(count+1, boba_names[count], boba_prices[count]))
    