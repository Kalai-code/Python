# working solution
def balancedStringSplit(s: str) -> int:
    l_count = r_count = split_count = 0
    for ch in s:
        if ch == "L":
            l_count = l_count + 1
        else:
            r_count = r_count + 1
        if l_count == r_count:
            split_count = split_count + 1
    return split_count


print(balancedStringSplit("LLLLRRRR"))