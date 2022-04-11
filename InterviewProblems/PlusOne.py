# Problem 66. Plus One
from typing import List

def plusOne(digits: List[int]) -> List[int]:
    my_lst_int= ''.join(map(str, digits))
    my_lst_int = int(my_lst_int) + 1
    return list(map(int, str(my_lst_int)))
    
print(plusOne([1,2,3]))

print(plusOne([4,3,2,1]))

print(plusOne([9]))