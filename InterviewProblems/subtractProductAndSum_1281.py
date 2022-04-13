import math
from functools import reduce
# solution 1
def subtractProductAndSum_bkup(n: int) -> int:
    res = list(map(int,str(n)))
    sumDigits = 0
    prodDigits = 1
    for x in res:
        prodDigits = prodDigits * x
        sumDigits = sumDigits + x
    return prodDigits - sumDigits

# solution 2 - using math functions  
def subtractProductAndSum(n: int) -> int:
    res = list(map(int,str(n)))
    sumDigits = sum(res)
    prodDigits = math.prod(res)
    return prodDigits - sumDigits

#solution 3 - using lambda
def subtractProductAndSum(n: int) -> int:
    res = list(map(int,str(n)))
    sumDigits = reduce((lambda x, y: x + y), res)
    prodDigits = reduce((lambda x, y: x * y), res)
    return prodDigits - sumDigits
    
print(subtractProductAndSum(234))

print(subtractProductAndSum(4421))