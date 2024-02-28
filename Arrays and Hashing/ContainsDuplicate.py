"Time complexity: O(n) for loop, can only grow to size of input array nums"
'Space complexity: O(n) worst case, set can only grow to size of input array nums'


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        noDups = set()
        for i in nums:
            if i in noDups:
                return True
            noDups.add(i)
        return False
