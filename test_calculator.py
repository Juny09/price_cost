from calculator import calculate_selling_price


cost = 100
margin = 30

price = calculate_selling_price(cost, margin)

print("Cost: RM", cost)
print("Margin:", margin, "%")
print("Selling Price: RM", price)