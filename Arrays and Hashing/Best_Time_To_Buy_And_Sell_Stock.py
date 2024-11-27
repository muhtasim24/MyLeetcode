'''
so we are given an array prices where prices[i] is the price of a given stock on the ith day
we want to maximize profit by buying one day and selling on another day
we want to get the max profit we could make
[7, 1, 5, 3, 6, 4] so lets we buy at 1, and sell at 6, so 6-1 = 5, thats our profit
of course we have to buy first before we sell
so lets say we have 2 pointers 
1 pointer is continsouly going
and another pointer is stayed at the smallest value we've seen so far
and of coure we are tracking the profit everytime the continous pointer upadtes

so we have pointer buy and sell
sell keeps going
if prices[sell] < prices[buy], we set buy to sell
and keep going



'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        maxProfit = 0

        for sell in range(len(prices)):
            profit = prices[sell] - prices[buy]
            maxProfit = max(profit, maxProfit)

            if prices[sell] < prices[buy]:
                buy = sell
        return maxProfit
        
