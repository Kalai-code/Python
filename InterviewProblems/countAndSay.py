def countAndSay(n: int) -> str:
    increment_count = 2
    temp_str = "1"   
    while increment_count <= n:
        outStr = ""
        for i in temp_str:
            outStr = outStr + i + str(temp_str.count(i))
        temp_str = outStr
        increment_count = increment_count + 1
    return temp_str

print(countAndSay(3))