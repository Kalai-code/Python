# code to write odd numbers from 1 to 100 in  oddNumbers.txt and even numbers from 1 to 100 in evenNumbers.txt file.

import os

"""
odd_fileName = "oddNumber.txt"
even_fileName = "evenNumber.txt"
"""

odd_fileName = "C:\\PythonLearning\\TextFiles\\oddNumbers.txt"
even_fileName = "C:\\PythonLearning\\TextFiles\\evenNumbers.txt"
oddfile_open = open(odd_fileName,'w')
oddfile_open.write("Odd Numbers:\n\n")
evenfile_open = open(even_fileName,'w')
evenfile_open.write("Even numbers:\n\n")
for num in range(1,101):
    if num % 2 == 0:
        evenfile_open.write(str(num)+"\n")
    else:
        oddfile_open.write(str(num)+"\n")
       
oddfile_open.close()
evenfile_open.close()


