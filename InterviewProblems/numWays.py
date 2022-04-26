def numWays(s: str) -> int:
    count_1 = s.count('1') / 3
    outputNum = 0
    current_str = ""
    for ch in s:
        if ch == '1':
            current_str = current_str + ch
            if current_str.count('1') == count_1:
                outputNum = outputNum + 1
                current_str = ""
        else:
            current_str = current_str + ch
    return outputNum


print(numWays("10101"))