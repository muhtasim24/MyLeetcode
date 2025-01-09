'''
We are given n gas stations along a circular
the amount of gas u get from each gas station is at gas[i]
the cost to travel to the next station is at cost[i]
You begin with an empty tank

we are given 2 int arrays, gas and cost
we have to return the starting gas station index, where we can start from and do a complete loop
and stop at the station we started from

ex:
gas = [1, 2, 3, 4, 5],   cost = [3, 4, 5, 1, 2]
the output starts at index 3, why? 
so if we start at gas[0] = 1, and the cost[0] = 3, we do not have enough gas to get to the next station
so lets try gas[1] = 2, it costs[1] = 4, still not enough to get to the nex tstation
gas[2] = 3, cost[2] = 5, not enough
gas[3] = 4, cost[3] = 1, we have enough
so now we can start our algo, we found starting position
so we can get to the next station :
if gas[i] >= cost[i] for our starting point, after that we can keep a running sum of our tank
so now our tank = 0 + 4 = 4

to get to the next station: 
it costs 1 so tank = 4 - 1 = 3, but we reached the ext station, so we can take the gas amount in that index
so tank = 3 + 5 = 8
can we get to next station? 
it will cost 2,
we have 8, yes we can
tank = 8 - 2 + 1 = 7
so everytime we get to the next station, save the previous cost
so tank = tank - cost[previous] + gas[current]
now if tank >= cost, we can contisnouly go to next station
we can have a while loop

while tank >= cost[i]:
    if startIndex == i:
        return True
    do the calculation
else False
------------------------------------------------------------------------------------------------------------------------------
ABOVE IS BRUTE FORCE O(n^2), passing 34/39 test cases

so lets do one better, Greedy O(n) solution
so with our 2 given arrasy, gas and cost
we can assume there can only be a solution, IF the sum of gas array is >= sum of cost array
because lets say the sum of our cost array is larger, then we know for sure, we can never do a loop
Edge case to return -1 right at the beginning

now we can initlize a total and a result index
we will go through every element
for every element we will check
total = gas[index] - cost[index]
if total > 0, if its not,
if total is smaller than 0 , htat menas we dont have enough gas,
so that means our current index is not a solution, go to the next
we are GARAUNTEED a solution if we get through the first check between sums 

so if the current index is not a solution, we will reset our total = 0
and update our index to the next one 
if total ever becomes negative when going through the arrays, then that index not valid solution


'''


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if we even have a valid solution
        # sum of gas array has to be larger than sum of cost array
        # if sum(cost) >, then we know we cant do a loop
        if sum(gas) < sum(cost):
            return -1

        #initlize total and result index
        total = 0
        res = 0

        for i in range(len(gas)): 
            # gas we have - cost it will take to get to next station
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        # we are garanteed solution so we can just return the res eventually when we find it
        # we will check if from our starting index, our total never becomes negative as we reach the end 
        # of the arrays 
        # if starting index, total becomes negative,
        # we update our starting index
        # we never actually loop
        # we just assume, if we can reach the end of the list without total becoming negative
        # we have enough to to do the loop, because sum(gas) > sum(cost)
        return res
                    

