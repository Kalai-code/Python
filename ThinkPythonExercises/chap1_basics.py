print("Hello, World!!")
# Exercise 1-1
#what happens when we leave out one of the parentheses or both in print statement
# Output Message: SyntaxError: unexpected EOF while parsing --> for end parentheses missing
# Output Message: SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Testing parentheses")) --> for beginning parentheses
# Output Message: SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Testing parentheses")? --> for both parentheses
print ("Testing parentheses")

# what happens when we leave out quotation marks, one or both in print statement
# Output Message: SyntaxError: EOL while scanning string literal --> for missing quotation mark at the end
# Output Message: SyntaxError: invalid syntax --> for missing quotation mark in the beginning of the string and for both the quotation marks
print("Testing quotation marks")

#Testing minus(-) and plus(+) sign before a number

a = -2
print(a) # output: -2

b = +2
print(b) #output: 2

# 2++2 --> 4
# 2--2 --> 4
# 2+-2 --> 0
# 2-+2 --> 0
c = 2++2
print(c)

#Exercise 1-2
#1. How many seconds are in 42 minutes ans 42 seconds

seconds = (42*60)+ 42
print("There are " + str(seconds) + " seconds")

#2. How many miles in 10 kilometers - 1.61km in a miles

miles = (10 / 1.61)
print("Number of miles in 10 kilometers is " + str(miles) + " miles")
 