from colorama import Fore, Back, Style, init

# List to store ordered pizzas
order_list = ['Original Milk Tea', 'Black Tea', 'Grape Slushy', 'Pineapple Slushy']

# List to store pizza prices
order_cost = [8.00, 7.20, 9.20, 9.20]

# Customer details
customer_details = {'name': 'Rhamz Dela Torre', 'phone': '021021021', 'house': '17Gabe', 'street': 'Rhamz', 'suburb': 'Aaron'}
init(autoreset=True)

def print_order():
    print()
    # Print customer order
    print(Fore.GREEN + "Customer Details")
    print(f"Customer Name: {customer_details['name']}\nCustomer Phone: {customer_details['phone']}\nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print(Fore.GREEN + "Order Details")
    count = 0
    for item in order_list:
        print(Style.BRIGHT + "Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()

print_order()