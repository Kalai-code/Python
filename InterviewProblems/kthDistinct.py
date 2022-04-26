from typing import List
# working solution
"""

"""
def kthDistinct(arr: List[str], k: int) -> str:
    distinct_arr = [i for i in arr if arr.count(i) == 1]
    if len(distinct_arr) >= k:
        return distinct_arr[k-1]
    else:
        return ""


print(kthDistinct(["a","b","a"],3))