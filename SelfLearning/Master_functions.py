# program to print numbers 1 to 10
def print_numbers():
	num = 1
	while num <= 10:
		print(num)
		num +=1
        
# Program to add two numbers
def add_numbers(num1,num2):
    total = num1 + num2
    return total

# Maximum of two numbers in Python
def max_twonumbers(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

#Python Program for factorial of a number
def factorial(num):
    fact = num
    if num == 0 or num == 1:
        return 1
    else:
        while num >1:
            num = num - 1
            fact = fact * (num)
        return fact
            
    