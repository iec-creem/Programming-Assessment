# List to store ordered pizzas
order_list = ['Original Milk Tea', 'Black Tea', 'Grape Slushy', 'Pineapple Slushy']

# List to store pizza prices
order_cost = [8.00, 7.20, 9.20, 9.20]

# Customer details
customer_details = {'name': 'Rhamz Dela Torre', 'phone': '021021021', 'house': '17Gabe', 'street': 'Rhamz', 'suburb': 'Aaron'}

print(customer_details)

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1