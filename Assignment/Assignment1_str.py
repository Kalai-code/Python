# 3/21/2022 string assignment

# Assignment 1
#split the domain name from the emailID
print("\nAssignment 1\n")
email="abc.aaa.123@gmail.com"
substring = email[email.find('@') + 1:] 
domain = substring[:substring.find('.')]
print("Email:",email)
print("Domain:",domain)

email="abc_aaa@yahoo.co.in"
substring = email[email.find('@') + 1:] 
domain = substring[:substring.find('.')]
print("\n")
print("Email:",email)
print("Domain:",domain)

email="abc_______123@testing.in"
substring = email[email.find('@') + 1:] 
domain = substring[:substring.find('.')]
print("\n")
print("Email:",email)
print("Domain:",domain)

# Assignment 2
# Get the name of the person from the string
print("\nAssignment 2\n")
content = "Dear User1, welcome to the program"
text1 = content[content.find(' ') + 1:]
person_name = text1[:text1.find(',')]
print("\nText:",content)
print("\nName:",person_name)

content = "Dear SuperUser2, welcome to the program"
text1 = content[content.find(' ') + 1:]
person_name = text1[:text1.find(',')]
print("\nText:",content)
print("\nName:",person_name)

