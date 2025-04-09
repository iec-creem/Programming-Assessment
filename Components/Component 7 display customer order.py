# List to store ordered pizzas
order_list = ['Original Milk Tea', 'Black Tea', 'Grape Slushy', 'Pineapple Slushy']

# List to store pizza prices
order_cost = [8.00, 7.20, 9.20, 9.20]

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1