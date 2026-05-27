grocery_inventory={
	"Milk":(113,"Dairy"),
	"Eggs":(116,"Dairy"),
	"Bread":(117,"Bakery"),
	"Apple":(141,"Produce")
}
bread_details= grocery_inventory.get("Bread")
print(Detaiks of Bread",["Brad"])
grocery_inventory.update({"Cookies":(143,"Bakery")})
grocery_inventory.pop("Eggs")
print("Details of Bread:",["Bread"])
print("Inventory after adding Cookies:",grocery_inventory)
print("Inventory after removig Eggs", '{)