# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}
discount_threshold = 100
print("Processing started")
for item in inventory:
	current_stock, minimum_required_stock, restock_quantity, sales_status= inventory[item]
	print (f"Processing {item}")
	while current_stock < minimum_required_stock:
		current_stock += restock_quantity
		inventory[item][0]= current_stock
	if current_stock> discount_threshold:
		sales_status=True
		inventory[item][3]= sales_status
print("Processing completed")
	
	