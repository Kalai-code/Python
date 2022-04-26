def countEven(num: int) -> int:
        count = 0
        for num in range(2,num+1):
            num_list = list(map(int,str(num)))
            print(num_list)
            print(sum(num_list))
            if sum(num_list) % 2 ==0:
                count = count + 1
        return count
        
print(countEven(30))