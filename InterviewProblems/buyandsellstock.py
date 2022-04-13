#problem 121. Best Time to Buy and Sell Stock

from typing import List

def maxProfit(prices: List[int]) -> int:
    max_Profit = 0
    for i in range(len(prices) - 1):
        for j in range(i+1,len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_Profit:
                max_Profit = profit
                
    return max_Profit
    

print(maxProfit([7,1,5,3,6,4]))