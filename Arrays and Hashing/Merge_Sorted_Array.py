'''
we are given 2 integer arrays nums1 and nums2, sorted in non-decreasing order
we have to merge nums1 and nums2 into a sorted order
we want to store the merged array into nums1, so dont return anything
nums1 has a length of m+n, the m elements denote the elemtns that should be merged
the last n elements are set to 0, and are ignored
nums2 has a length of n

ex:
nums1 = [1,2,3,0,0,0] m = 3, nums2= [2, 5, 6] n = 3
[1, 2, 2, 3, 5, 6], so how do we just append nums2 into nums1 sorted
2 pointers?
maybe we could go backwards, 
since nums1 has 3 slots where we could put in the values that would fit correctly

we are also given m and n
so we have 2 pointers, one at index m
and the other at index n
we iterate through nums1 backwards
nums1=[1, 2, 3, 0, 0, 0]        nums2 =[2, 5, 6] 
             m         i                      n
we compare m and n
if n is larger than m, we insert n and at where i currently is
if n is smaller than m, we insert m at where i currently is 
so since n is larger than m, n would go to i
nums1=[1, 2, 3, 0, 0, 6]        nums2 =[2, 5, 6] 
             m     i                       n
m stays where it is, cause n was larger
if m was larger then we would update m
but since n was larger, we update n 
now is n(5) > m(3), yes so n goes where i is

nums1=[1, 2, 3, 0, 5, 6]        nums2 =[2, 5, 6] 
             m  i                       n
n > m, NO
n < M, yes so m goes where i is, 
nums1=[1, 2, 2, 3, 5, 6]        nums2 =[2, 5, 6] 
          m  i                          n
so what happens at m, do we go back? i think so
is m > n, no 
is n < m, 
if its equal just take n, 
so maybe we could combine if 
we would do this until n can no longer go

we start from the end beasue we bascailly have avaible positions to insert values
if we start from the beginning, we have to save the value we are removing, insert a value
but what happens to the value we removed, gets complicated

'''



class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[0] = nums2[0]

        pointN = n - 1 # pointer n is at last index of nums2
        pointM = m - 1 # pointer m is at last index of nums1, without the 0s
        end = m + n - 1 # pointer at the end of list of nums1 at m + n
        
        print(nums1[pointM])
        # while we havent reached the end of nums2:
        while pointN >= 0:
            # we can make our comparisons
            # if n > m, we put n were end is 
            # and update n 
            
            # if n < m, we put m where end is
            # and update m
            # we do pointM >= 0, in the case, where m is 0 or below, most likely will be 0 if there
            # is nothing in nums1, as in no elmenets of nums1 has m elements, so it only has
            # space for n elements
            if pointM >= 0 and nums2[pointN] < nums1[pointM]:
                nums1[end] = nums1[pointM]
                pointM -= 1
            # if m >= n or m <= n
            # we will choose to put n in 
            else:
                nums1[end] = nums2[pointN]
                pointN -= 1

            end -= 1

        
