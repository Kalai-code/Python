class Printnumbers:
    """A simple class to print numbers from 1 to num(userinput)"""
    
    def __init__(self,num):
        self.num = num
        
    def print_numbers(self):
        for n in range(1,self.num + 1):
            print(n)
            
print_nums = Printnumbers(20)
print_nums.print_numbers()