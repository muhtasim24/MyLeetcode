'''
need to buy before we can sell
we need max profit, so keep track of that 


so we need L at the beginning, and the right pointer 1 more ahead of L at the start 

[7, 1, 5, 3, 6, 4]
 L  R
so L is at 7 
and R is at 1
L will be for buy
R will be for sell
why would we buy from L when R is smaller, we want to buy low and sell high 
so update L and R

[7, 1, 5, 3, 6, 4]
    L  R
so we buy at 1 now and sell at 5, maxProfit is 4, cuz 5-1 = 4
maxProfit = 4
update R, keep L the same cause we havent found a point where R is less than L

[7, 1, 5, 3, 6, 4]
    L     R
profit is 3-1 = 2, dont update maxProfit
move on to next with R

[7, 1, 5, 3, 6, 4]
    L        R
profit is 6 - 1 = 5. we found a higher profit, update maxProfit = 5
move R
and we reached the last element, it wont be a new max cause 4-1 = 3 

and we just return maxProfit


'''



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        L, R = 0, 1

        while R < len(prices):
            #have to make sure its profitable first
            #left has to be lower than R
            if prices[L] < prices[R]: 
                profit = prices[R] - prices[L]
                currMax = max(currMax, profit)
            
            #its not profitable that means value of R is less than value of L
            #so just update L to where R is 
            else:
                L = R
            #and we always want to update R 
            R += 1
        return currMax
        
        return currMax
        
