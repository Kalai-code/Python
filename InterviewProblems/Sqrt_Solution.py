def mySqrt(x: int) -> int:
    num = 1
    sqrt = 0
    while sqrt <= x:
        sqrt = num * num
        if sqrt < x:
            num = num + 1
        elif sqrt == x:
            return num
        else:
            return num - 1
            
#Example Testcases
# x = 4 Output: 2
print(mySqrt(4))

# x = 8 Output: 2
print(mySqrt(8))

# x = 0 Output: 0
print(mySqrt(0))