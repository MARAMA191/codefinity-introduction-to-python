# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count=shelf.count("apples")
print("Number of apple: ", apple_count)
banana_index=shelf.index("banana")
if apple_count<5 :
	print ("Apples need to be restocked")
else :
	print("Apples are sufficiently stocked")
grapes_count=shelf.count("grapes")
if grapes_count=1:
	print(