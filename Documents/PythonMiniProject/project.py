# Python mini project QA 
coffee_list = ['Espresso','Americano','Cappuccino']
num_drinks = 0
DRINK_PRICE = 2.50
order_total = 0
items = False
active = True 
# Prints the menu for the user 
print(f"Menu {coffee_list}")
# Beginning of main menu loop 
while active:
    # Prompt user for input and gives instruction 
    print("Choose a drink from the menu, enter x to exit, or c to checkout")
    # Loop that prints menu items 
    for i in coffee_list:
        print(i)
    while True:
        # Save user input 
        order = input("Selection: ")
        # If user decides to exit quits the program 
        if order == "x":
            print("Thank you and goodbye")
            quit()
        # If selection in menu increment order amount and add totals 
        elif order in coffee_list:
            num_drinks = num_drinks + 1
            items = True

            order_total = order_total + DRINK_PRICE
            # Display cart to user 
            print(f"{order} added to cart, you have {num_drinks} drink(s) in your cart, order total ${order_total}")
        # Handles user checkout 
        elif order == "c":
            # Checks if order contains items 
            if items == False:
                print("No items in cart, you cannot checkout")
            else:
                # Prints order details and exits the program 
                print(f"Order total ${order_total}, please pay at till, thank you.")
                quit()
        elif order == "o":
            if num_drinks > 0:
                print(f"you have {num_drinks} drink(s) in your cart, order total ${order_total}")
            else: 
                print("Order details not available, add items to cart and try again")
        # Inform user of error when they enter item that doesn't exist
        else:
         print("Sorry that is not available")
    
        break