# Problem - 263. Ugly Number
"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""
def isUgly(n: int) -> bool:
    flag = False
    if n in range(1,7):
        return True
    else:
        limitNum = int(n / 2)
        for i in range(2,limitNum + 1):
            if n % i == 0 and (i == 2 or i == 3 or i==5):
                flag = True
            else:
                flag = False
        return flag
        
print(isUgly(14))
print(isUgly(9))
print(isUgly(10))