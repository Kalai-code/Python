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
print("Length:",lenList)

num = ''.join(numList)
print(num)


text = "hello"
txtList = list(map(str,text))
print(txtList)

txt = ''.join(txtList) # joins the list and returns string as output
print(txt)