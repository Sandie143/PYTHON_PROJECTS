cost=float(input("amount charge for the food: "))
tip=cost*.18
print('tip: %.2f'% tip)
sales_tax = cost*.7
print('sales_tax: %.2f'% sales_tax)
total=cost + tip + sales_tax
print("total: ", total)