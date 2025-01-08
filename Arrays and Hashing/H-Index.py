'''
we are given an array of integers, citations
each element is the # of citations for their ith paper
we have to return the max value of h such that the researcher has published 
at least h papers that each have been cited at least h times
so the max h is always less than or equal to the # of publications

H = # of publications and # of citations 
[3, 0, 6, 1, 5] 
lets see why our output is 3
h-index: 0, we cant have greater than 0 so nothing
h-index: 1, we have index 3, with a value of 1, that makes this good, so 1 is a 
possible h-index we can return, but is it the MAX?

h-index: 2
we have index 0,(3), index 1 (6), so we have at least 2 papers that have at least 2 citations
2 works
h-index: 3
we have index 0, (3), index 1 (6) , index4 (5) with at least 3 citations
for the h-index, we want to find the h-index # of papers with at least that many citations
so 3 is a possible value we can return because 
with the h-index of 3 
we have at LEAST 3 papers with 3 citations
h-index: 4
we have only index 1 (6), and index 4 (5) with at least 4 citations
for h-index 4 to be a possible h, we needed 4 papers with at least 4 citations 

and the max h value we could have is 5
because there are 5 papers, and if all papers had at least 5 citations
our max h val would be 5, but they dont so its not 5

so now that we understand the problem
how can we solve it
we can have a citations bucket
each index will represent citations, and each value will represent how many papers have that 
number of citations
for [3, 0, 6, 1, 5] 
        citations   0  1  2. 3. 4. 5 
citations_bucket = [0, 0, 0, 0, 0, 0]
                    1. 1. 0. 1. 0. 2
the last index will be seen as at least 
so if the value is higher than length of array, we can put it at last index

once we created this bucket
we can iterate through it 
and have a running count of papers
but lets do it in reverse, because we want the largest h-value
start papers equal to num of papers at the last index
        citations   0  1  2. 3. 4. 5 
citations_bucket = [0, 0, 0, 0, 0, 0]
                    1. 1. 0. 1. 0. 2
                                   p
papers = 2, so if # of papers is not >= index, its not a valid h-value so we have to move on
so if papers >= current index:
    then we can return
else: papers is not greater or equal to the index
we will go down to hte next index
        citations   0  1  2. 3. 4. 5 
citations_bucket = [0, 0, 0, 0, 0, 0]
                    1. 1. 0. 1. 0. 2
                                p
papers = 2, stays at 2 since 4 has no citations

        citations   0  1  2. 3. 4. 5 
citations_bucket = [0, 0, 0, 0, 0, 0]
                    1. 1. 0. 1. 0. 2
                             p
papers = 3 increments to 3, since at citatiosn3 , we have 3 papers, so we found our valid h-value
return 
that is the highest we will get, no point of going lower


Time: O(n), did one pass through input array
Space: O(n), created an array of size n + 1, n being length of input array, so O(n)


'''


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_bucket = [0] * (len(citations) + 1)

        # want to put in citation to their respective index
        # so if value 3, should go to index 3 and increment 1
        print(citations_bucket)
        for citation in citations:
            if citation > len(citations):
                citations_bucket[-1] += 1
            else:
                print(citation)
                citations_bucket[citation] += 1

        # now we have craeted the bucket, where each index is the # of citations 
        # and each index we have the # of papers that have that many citations

        # now we can iterate in reverse to find a valid h-val
        papers = 0
        for i in range(len(citations_bucket)-1, -1, -1):
            papers += citations_bucket[i]
            if papers >= i:
                return i
