prices = [29.99, 45.50, 12.75, 38.20]
discounts=[0.10,0.20,0.15,0.05]
for i in range(len(prices)):
	new_price =prices[i]*(1-discounts[i])
	print(f"Updated price for index {i}: new_price[i]")