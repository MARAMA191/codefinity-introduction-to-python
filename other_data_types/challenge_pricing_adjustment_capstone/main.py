grocery_inventory= {
    "Milk": ("Dairy",3.50,8),
    "Eggs": ("Dairy",5.50,30),
    "Bread": ("Bakery",2.99,15),
    "Apples": ("Produce",1.50,50)}
if grocery_inventory["Eggs"][1]>5:
print("Eggs are too expensive, reducing the price by $1")