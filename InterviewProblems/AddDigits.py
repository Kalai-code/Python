# Problem 258. Add Digits
#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

def addDigits(num: int) -> int:
    numList = list(map(int, str(num)))
    sumNum = sum(numList)
    while sumNum >= 10:
        sumNum = sum(list(map(int, str(sumNum))))
    return sumNum
    
print(addDigits(38))

print(addDigits(0))