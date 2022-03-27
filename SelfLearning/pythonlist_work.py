#list in python

numbers = ["one","two","three","four","five"]
print(numbers[0])
print(numbers[-1])

print(numbers[0].title())

numbers.append("six")
print(numbers[-1])

numbers.insert(1,"newnumber")
print(numbers[1])

del numbers[1]
print(numbers[1])

#for loop example
#print all the elements in the list
print("Print all the elements in the list")
for i in numbers:
    print(i)
   
# pop an item from the list
# pop() --> pops the item from the list and pop(1) --> pops the specific items from the list.
print("pop method in Python")
number_pop = numbers.pop()
print(number_pop)

number_pop = numbers.pop(1)
print(number_pop)

print("Print the elements in the list after using pop method")
for i in numbers:
    print(i)
    

#Try it yourself
names = ['arun','mithra','shatvik']
for name in names:
    print(f"Hello, {name.title()}")

#Try it yourself list
print("\t exercise 3.4")
names = ['arun','mithra','shatvik']
for name in names:
    print(f"Hi {name.title()}, I would like to invite you for dinner.")

print(f"Hi All, {names[0].title()} wont be able to join us for dinner.")

names[0] = "kalai"
for name in names:
    print(f"Hi {name.title()}, I would like to invite you for dinner.")
    
print(f"Good news!! I have found a bigger dining table so we can have more people")
names.insert(0,'Arun')
names.insert(2,'kumar')
names.append('chitra')
for name in names:
    print(f"Hi {name.title()}, I would like to invite you for dinner.")
print("New dining table will not arrive on time. Sorry about it")
print("\tnew list")
for name in names:
    print(name)


while len(names) > 2:
        print(len(names))
        pop_name = names.pop()
        print(f"Hi {pop_name.title()}, we shall catch up again")
for name in names:
    print(f"Hi {name.title()}, I would like to invite you for dinner.")
    
#try it yourself
print("Seeing the World")
locations = ['America','Canada','UK','India','Australia']
print("\t Original list")
print(locations)
print("\n\t Sorted list using sorted method")
print(sorted(locations))
print("\n\t Original list")
print(locations)
print("\n\t Sorted list using sorted method and reverse")
print(sorted(locations,reverse=True))
print("\n\t Original list")
print(locations)
print("\n\t Reverse the list")
locations.reverse()
print(locations)

print("\n\t Reverse the list to match original list")
locations.reverse()
print(locations)

print("\n\t sort the list")
locations.sort()
print(locations)

print("\n\t sort the list in reverse")
locations.sort(reverse = True)
print(locations)

#Try it yourself Pizza
print("\n\tTry it yourself Pizza")
pizzas = ['veggie', 'chicken', 'pepperoni']
for pizza in pizzas:
    print(f"I like {pizza} pizza a lot")
print("I really love pizza")

#Range function
for value in range(0,6):
    print(value)
    
#list using range function
numbers = list(range(2,11,2))
print(numbers)

#list for generating square root value
squares = []
for number in range(1,11):
    squares.append(number**2)
print(squares)

#min,max and sum of digits 0 to 9
numbers = list(range(0,10))
print("Min:",min(numbers))
print("Max:",max(numbers))
print("Sum:",sum(numbers))

#Try it yourself print 1 to 20

for num in range(1,21):
    print(num)

#Try it yourself print odd numbers
for num in range(1,20,2):
    print(num)

#make a list of multiples of 3
three_numbers = list(range(3,31,3))
for num in three_numbers:
    print(num)
    
#cube comprehension
cubes = []
for num in range(1,11):
    cubes.append(num ** 3)
print(cubes)

my_foods = ['pizza','pasta','falafel','cake','noodles']
friend_foods = my_foods[:]
print("The first three items in the list are:")
for food in my_foods[0:3]:
    print(food)

print("The three items from the middle of the list are:")
for food in my_foods[1:4]:
    print(food)

print("The last three items of the list are:")
for food in my_foods[2:]:
    print(food)  

my_foods.append('fried rice')
friend_foods.append('burger')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)    
