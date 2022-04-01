# code to write odd numbers from 1 to 100 in  oddNumber.txt and even numbers from 1 to 100 in evenNumber.txt file.
import os

odd_fileName = "oddNumber.txt"
even_fileName = "evenNumber.txt"
oddfile_open = open(odd_fileName,'w')
oddfile_open.write("Odd Numbers")
evenfile_open = open(even_fileName,'w')
evenfile_open.write("Even numbers")
for num in range(1,101):
    if num % 2 == 0:
        evenfile_open.write(str(num))
    else:
        oddfile_open.write(str(num))
        
oddfile_open.close()
evenfile_open.close()