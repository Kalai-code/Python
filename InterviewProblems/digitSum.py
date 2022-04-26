def digitSum(s: str, k: int) -> str:
        inner_list = []
        str_len = len(s)
        while str_len > k:
            list_s=[]
            for i in range(0,len(s),k):
                split_str = s[i:i+k]
                inner_list = list(map(int,split_str))
                list_s.append(sum(inner_list))
            s = "".join(map(str,list_s))
            str_len = len(s)
        return s


print(digitSum("1234",2))