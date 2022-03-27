#string can be enclosed in single or double quotes. Both works
#single line comment using #symbol
#multiline comment use three double or single quotes at the beginning and end of the comment

#variable doesnt need declaration
message = "Learn string in python"
print(message)
#to give a line break use \n
print("\n")
print("\tHello")

#captilizes first letter of every word to upper case
print(message.title())

#convert the string to lower case
print(message.lower())

#convert string to upper case
print(message.upper())

#f is for formatting a string
first_name = "harry"
last_name = "potter"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#The below code also return the same response as f formatting
first_name = "harry"
last_name = "potter"
full_name = first_name + ' ' + last_name
print(f"Hello, {full_name.title()}!")

#strip() is for trimming any extra white spaces in a string
#lstrip() is to trim extra space on left of a string
#rstrip() is to trim extra space on right of the string
new_text = " Remove extra spaces "
print(new_text.strip())
print(new_text.lstrip())
print(new_text.rstrip())

#try it yourself
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

name = "eric Peter"
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)

message = f"Hello {name.lower()}, would you like to learn some Python today?"
print(message)

message = f"Hello {name.upper()}, would you like to learn some Python today?"
print(message)

quote = "Albert Einstein once said, \"A person who never made a mistake never tried anything new\"."

print(quote)

famous_person = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."
output = f"{famous_person} once said, \"{message}\""
print(output)

#try it yourself
mynumber = 2
print(f"My favorite number is {mynumber}")

#Arithmetic operations
print(5+3)
print(11-3)
print(4*2)
print(24/8)