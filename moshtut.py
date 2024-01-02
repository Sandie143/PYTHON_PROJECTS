#price of house is 1million
#if buyer has good credit ,they need to put down 10%
#otherwise buyer needs toput down 20%
#print the down payment

price_of_house = 1000000
has_good_credit= True
if has_good_credit : 
    down_payment=0.1 * price_of_house
else:
    down_payment=0.2 * price_of_house

print(f"down payment: ${down_payment}")   

    

 