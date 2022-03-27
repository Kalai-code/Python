# Try it yourself if statements in python
car = "audi"
if car == "audi":
    print(f"\n The car is {car}")
else:
    print("\n The car is not audi")

print(car == "subaru")

list_fruits = ['apple','orange','banana','grapes']
for fruit in list_fruits:
    if fruit == 'banana':
        print(f"{fruit.title()} is my favorite fruit")
if 'apple' in list_fruits:
    print("True")

if 'melon'  not in list_fruits:
    print("False")
    
# Try it yourself 2
alien_colors = ['green','yellow','red']
for color in alien_colors:
    if color == 'green':
        print("The player has earned 5 points")
    elif color == 'yellow':
        print("The player has earned 10 points")
    elif color == 'red':
        print("The player has earned 15 points") 


age = 70
if age <= 2:
    print("He/She is a baby")    
elif age > 2 and age <=4:
    print("He/She is a toddler")
elif age > 4 and age <= 13:
    print("He/She is a kid")
elif age > 13 and age <=20:
    print("He/She is a teenager")
elif age > 20 and age <=65:
    print("He/She is an adult")
elif age>65:
    print("He/She is an elder")
    
#Try it yourself "Hello Admin"
#usernames = ['Adam','Alex','Admin','Ben','Harry']
usernames = []
if len(usernames) == 0:
    print("We need to find some users!")
else:
    for name in usernames:
        if name == 'Admin':
            print(f"\nHello {name}.title(), would you like to see a status report?")
        else:
            print(f"\n Hello {name}.title(), thank you for logging in again.")

# Try it yourself checking usernames
current_users = ['Jan','John','Alex','Andrew','Phil']
new_users = ['John','Bill','Phil','June','Ryan']
nuser = ''
for user in new_users:
    if user in current_users:
        print(f"{user} already exists, please enter a new username")
    else:
        print(f"{user} is available")
        
#Try it yourself Ordinal numbers
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(str(number)+'st')
    elif number == 2:
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')