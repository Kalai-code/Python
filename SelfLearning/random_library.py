from random import randint, choice
#Try it yourself to use Python standard library - Dice
class Dice:
    """Class file to roll a dice and get a random number"""
    
    def __init__(self,sides = 6):
        self.sides = sides
        
    def dice_randomnum(self):
        return randint(1,self.sides)

dice_num = Dice()
print(dice_num.dice_randomnum())
     
dice_num10 = Dice(10)
print(dice_num10.dice_randomnum())

dice_num20 = Dice(20)
print(dice_num20.dice_randomnum())

# Try it yourself - lottery
lottery_list = [2,4,6,8,1,3,5,11,14,18,'R','A','S','M','K']
first = choice(lottery_list)
second = choice(lottery_list)
third = choice(lottery_list)
fourth = choice(lottery_list)

print(f"Any ticket matching these four - {first}{second}{third}{fourth} letters or numbers wins the prize")