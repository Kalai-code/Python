import sys
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
def reverse(x: int) -> int:
        negative = False
        maxSize = (2 ** 31) - 1
        minSize = -(2 ** 31)
        if x < 0:
            negative = True
            x = abs(x)
        xlist = list(map(int,str(x)))
        xlist.reverse()
        xoutput = ''.join(map(str,xlist))
        xoutput = int(xoutput)
        if negative == True:
            if -abs(xoutput) < minSize:
                return 0
            else:
                return -abs(xoutput)
        else:
            if xoutput > maxSize:
                return 0
            else:
                return xoutput
                
print(reverse(1534236469))