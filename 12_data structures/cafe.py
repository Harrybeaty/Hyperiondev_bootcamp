total_stock = 0                                     # Initialise variable for later use. 
menu = ["Pizza", "Panini", "Burger", "Sandwich"]    # Create list of menu items
stock = {                                           # Create dictionary for stock.
    "Pizza" : 2,
    "Panini" : 4,
    "Burger" : 3,
    "Sandwich": 1
}
price= {                                            # Create dictionary for price.
    "Pizza" : 20.,
    "Panini" : 10,
    "Burger" : 15,
    "Sandwich": 8
}

for item in menu:                                   # Loop through each item in menu
    item_value = stock[item] * price[item]          # Use each item as the key in the dictionaries so that the correct stock is multiplied by the correct price.
    total_stock += item_value                       # Add each item value to the total stock

format_total_stock = "{:.2f}".format(total_stock)   # Format total stock as money.
print(f"Total stock: £{format_total_stock}")        # Print formatted total.