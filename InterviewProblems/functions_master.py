
#using arbitrary keyword arguments
def sandwich_topping(*toppings):
    for topping in toppings:
        print(f"Your order is: {topping}")
            