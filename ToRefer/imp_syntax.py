""" This file is to refer about important logic related to list,integer,string 
"""
import math
#convert int to a list of digits
num = 6521
numList = list(map(int,str(num))) # converts int to list
print(numList)
numList.sort() # sorts the list in ascending order
print(numList)

SumList = sum(numList) # return the sum of the list
print("Sum:", SumList)

prodList = math.prod(numList) # import math module to find the product of the list
print("Product:", prodList)

minNum = min(numList) # returns the minimum number from the list
print("Minimum:",minNum)

maxNum = max(numList) # returns the maximum number from the list
print("Minimum:",maxNum)

lenList =  len(numList)
print("Length:",lenList) # returns the length of the list

#code to convert int list to interger
# first convert int list to string and then convert to integer

intNum = ''.join(map(str,numList)) # converts int list to string
intNum = int(intNum) # convert to integer
print(intNum)



text = "hello"
txtList = list(map(str,text))
print(txtList)

txt = ''.join(txtList) # joins the list and returns string as output
print(txt)


# for loop to increment the number by 2
for i in range(0, 10, 2):
    print(i)
    
#code to convert character to number
text = "itsmycode"

# elegant way using list comprehension
num_list = [ord(x) - 96 for x in text]

# print the converted letters as numbers in list
print("After converting letters to numbers", num_list)

#code to convert number to character
print(chr(65)) # prints the character 'A'

# code to reverse a string
print("Hello"[::-1]) # prints olleH

# code to get reminder and quotient
quotient, reminder = divmod(12,6) # returns quotient = 2, reminder = 0