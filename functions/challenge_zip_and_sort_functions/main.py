# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]
# List of quantity sold
quantities_sold = [50, 100, 25, 40]
combined_list= zip( products, prices, quantities_sold)
sorted_products= sorted(combined_list)
for items in sorted_products:
	print(f"Product: {items[0]}")
	print(f"Price: {items[1]}"), print(f"Quantity Sold: {items[2]}")
