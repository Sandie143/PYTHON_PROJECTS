# -calculate the total price average for all products
# -create a new price list that reduces the old prices by $ 5
# -calculate the total revenue generated from the products
# -calculate the average daily revenue generated from the products
#  -based on the new prices, which products are less than $ 30 

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

mean= round(sum(prices)/len(prices),2)
print("the average total price for all products in the store is:$ ",mean)

new_price_list=[price-5 for price in prices]
print("the new price list reduced by 5:$ ",new_price_list)

total_revenue=sum(price * customers for price,customers in zip(prices, last_week) )
print(f"the total revenue generated from the products:$ {total_revenue}")

#assuming there are 7 days in a week
days=7
average_dialy_revenue=total_revenue/days
print(f"the average daily revenue generated from the products:$ {average_dialy_revenue}")

products_less_30=[]
for i in range (len(products)):
    if new_price_list [i] < 30: 
       products_less_30.append(products[i])
print("products less than 30 based on the new price: ",products_less_30)