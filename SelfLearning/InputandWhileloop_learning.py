# Learning how to read input from user and how to use while loop
'''
# How to read input from user - Try it yourself - Rental car
car_type=input("Please enter the car type which you would like to rent\n")
print(f"Let me see if I can find you a {car_type}")

# Restaurant Seating
number_people = input("Hi, How many people are in your dinner group\n")
number_people = int(number_people)
if number_people > 8:
    print("\nPlease wait to be seated")
else:
    print("\n The table is ready, please be seated")
    
#Check if a number is multiple of 10
number = input("Please enter a number\n")
number = int(number)
if number % 10 == 0:
    print("The given number is multiple of 10")
else:
    print("The given number is not a multiple of 10")
    


# While loop - Try it yourself - pizza toppings
message = "Please enter the toppings to be added in your pizza\n"
message += "Enter 'quit' when you are done\n" 
pizza_topping = ""
while pizza_topping != "quit":
    pizza_topping = input(message)
    if pizza_topping != "quit":
        print(f"{pizza_topping} is getting added to your pizza")

# Movie tickets
message_prompt = "Please enter the age to know the price of the movie ticket\n"
message_prompt += "Enter 'quit' when you are done"
age = ''

while age != 'quit':
    age = input(message_prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("The ticket is free")
        elif age >= 3 and  age < 12:
            print("The ticket price is $10")
        else:
            print("The ticket price is $15")

'''
# Try it yourself - Deli
sandwich_orders = ["veggie","pastrami","chicken","pastrami","tuna","pastrami","cheese"]
finished_sanwiches = []
current_order = ''
print("\n The store ran out of Pastrami sanwiches")
while "pastrami" in sandwich_orders:
     sandwich_orders.remove("pastrami")
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"\n I made your {current_order} sandwich")
    finished_sanwiches.append(current_order)

print("\n")
for sandwich in finished_sanwiches:
    print(f"Your {sandwich} is ready!")
    
