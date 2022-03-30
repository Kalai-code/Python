from typing import List
def isValid(s: str) -> bool:
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid."""
    stack = []
    if len(s) == 0:
        return False
    elif len(s) % 2 != 0:
        return False
    else:
        for ch in s:
            #print(ch)
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            #elif ch == ')' or ch == ']' or ch == '}':
            elif len(stack) > 0 and ch == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack) > 0 and ch == ']' and stack[-1] == '[':
                stack.pop()
            elif len(stack) > 0 and ch == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
                

# Test case 1 - Output: True            
print(isValid("()"))

# Test case 2 - Output: True  
print(isValid("()[]{}"))

# Test case 3 - Output: False  
print(isValid("(]"))

# Test case 4 - Output: False  
print(isValid("]("))