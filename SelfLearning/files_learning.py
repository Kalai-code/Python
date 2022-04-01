"""Learning how to read a file, append text to the file"""
file = "C:\\PythonLearning\\TextFiles\\sampleDoc.txt"
filename = "C:\\PythonLearning\\TextFiles\\writeDoc.txt"

# Read the entire file and print it

with open(file) as file_object:
    contents = file_object.read()
print(contents)

# Read the file line by line and print it
with open(file) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

for line in lines:  
    print(line.strip())
    
# Writing to a file - overwrites the existing text


with open(filename,'w') as file_object:
    file_object.write("I love programming.")
    

with open(filename,'a') as file_object:
    file_object.write("I love programming because they help me to think logically.")
    
with open(filename) as file_object:
    for line in file_object:
        print(line)
