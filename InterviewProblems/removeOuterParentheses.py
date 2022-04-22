def removeOuterParentheses(s: str) -> str:
    s = list(map(str,s))
    open = 0
    first_index = 0
    for i in range(0,len(s)):
        if s[i] == "(":
            open = open + 1
        elif s[i] == ")":
            open = open - 1
            if open == 0:
                s[first_index] = ""
                s[i] = ""
                first_index = i + 1
    return "".join(map(str,s))

print(removeOuterParentheses("(()())(())"))