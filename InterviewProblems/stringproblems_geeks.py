# string problem from GeeksforGeeks

#Python program to check whether the string is Symmetrical or Palindrome
print("\nPython program to check whether the string is Symmetrical or Palindrome")
text = "madam"
#symmetrical code
textlength = len(text)
if textlength % 2 == 0:
    val = int(textlength/2)
    s1 = text[:val]
    s2 = text[val :]
    if s1 == s2:
        print("\nThe given string is Symmetrical")
    else:
        print("\nThe given string is not Symmetrical")
else:
    print("\nThe given string is not Symmetrical")
#Palindrome code
revStr = ""
while textlength > 0:
    revStr = revStr + text[textlength - 1]
    textlength = textlength - 1
    
if text == revStr:
    print("\n The given string is palindrome")
else:
    print("\nThe given string is not palindrome")


#Reverse words in a given String in Python
print("\nReverse words in a given String in Python")
str = "i like this program very much"
revstr = ""
newstr = str.split()
strlen = len(newstr)
print(strlen)
while strlen > 0:
    revstr = revstr + ' ' + newstr[strlen - 1]
    strlen = strlen - 1  
print(revstr.strip())