import math
"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

#solution 1
def mySqrt(x: int) -> int:
        num = 1
        sqrt = 1
        if x== 0 or x == 1:
            return x
        while sqrt <= x:
            sqrt = num * num
            if sqrt < x:
                num = num + 1
            elif sqrt == x:
                return num
            else:
                return num - 1
"""
#solution 2
def mySqrt(x: int) -> int:
        if x == 1:
            return 1
        left = 0
        right = x//2
        while left <= right:
            mid = (left + right)//2
            print(mid)
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return math.trunc(right)

print(mySqrt(5))