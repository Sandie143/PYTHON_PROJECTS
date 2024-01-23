# -calculate the total price average for all products
# -create a new price list that reduces the old prices by $ 5
# -calculate the total revenue generated from the products
# -calculate the average daily revenue generated from the products
#  -based on the new prices, which products are less than $ 30 

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# -create a new price list that reduces the old prices by $ 5
#count the number of products
#find the sum total of all the product prices
#divide the sum total by the number of prodcts

num_products=len(products)
sum_total=sum(prices)
total_average=round(sum_total/ num_products,1)
print(num_products,sum_total,total_average)
print("The sum is ", sum_total,sep='$')

#-create a new price list that reduces the old prices by $ 5
#create an empty list 
#loop through te list and subtract 5 from each price
#append the new list with the new price 

new_price_list=[]
for price in prices:
    new_price_list.append(price-5)
print(new_price_list)