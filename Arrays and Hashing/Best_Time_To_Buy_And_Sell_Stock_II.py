'''
so we are given an integer array prices where prices[i] is the price of a given stock on the ith day
on each day we can either buy or sell, but have to buy before we sell
we can also sell same day we buy
we have to return the max profit we can make by buying and selling on the right momenets
buy low, sell high
so basically everytime we find a value that is higher than when we buy, we can make profit

so we can just use 1 pointer that goes through the entire prices array
compare the price that comes previously
if the price before is lower than the current price,
we can add to our total profit of the value we are at - value from previous day

so [7, 1, 5, 3, 6, 4]
we will strat at the 1st index not the 0th, sicne we area always comparing the previous index
cant compare previous index if we start at the 0th

so start at 1, 1 > 7, NO so nothing
5 > 1, yes , so do 5 - 1 = 4, to our profit profit is 4 rn
3 > 5, no, nothing
6 > 3, yes, so 6 - 3 = 3, so profit += 6 - 3, so profit is now 3 + 4 = 7
4 > 6, no 

works when all days are higher to
[1, 2, 3, 4, 5] 
2 > 1, yes, profit = 1
3 > 2, yes profit = 1 + (3 - 2) = 2
4 > 3, yes profit = 2 + (4-3) = 3
5 > 4, yes profit = 3 + (5-4) = 4
same as buying at 1 and selling at 5, profit = 5-1= 4, but in this case we made multiple transcation
for same result and fits more sitatuiosn


Time: O(n)
Space: O(1)


'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # start at first index, since we are comparing the previous index
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i-1]

        return profit
