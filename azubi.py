#A simple shopping cart prompting the user to add and remove variables .
shopping_cart=[]
while True:
    print("options")
    print("1. Add items to cart")
    print("2. Remove items from cart")
    print("3. View cart")
    print("4. Calculate the total cost")
    print("5. Quit")

    choice=input("enter the option you want: ")

    if choice == "1":   
        item_name=input("please enter the name of the product: ")
        item_price=input("enter the price of the product: ")
        shopping_cart.append({"name":item_name,"price":item_price })
    elif choice =="2":
        item_name=input("please enter the name of the product you want to remove: ")
        for item in shopping_cart:
           if item["name"]==item_name:
               shopping_cart.remove(item)
               print(f"{item_name} was removed")
               break
    elif choice =="3":
        print(shopping_cart) 
    elif choice =="4":
        total_cost=sum(int(item["price"])for item in shopping_cart)     
        print("$",total_cost)
    elif choice =="5":
        print("Thank you for shopping with us") 
        break   