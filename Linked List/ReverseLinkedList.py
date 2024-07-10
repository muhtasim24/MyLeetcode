'''
We are given a linked list, we just have to reverse it
We can use 2 pointers
1 pointer to track our previous node 
and 1 pointer to track our current node
prev will be initialized at None, and curr will be intialized at the head

To reverse, we will just set our current Node's .next to prev node
before setting the .next of our current node, we need to save the original current.next 
so we can update our pointers 
so curr.next will become prev
so prev will become curr 
and with saving curr.next in a temporary variable
curr = temp

by the time we reach the end of the linked list, our prev node will be where our new head is after 
reversing 

Time Complexity: O(n), going through entire input array once
Space Complexity: O(1) only using pointers
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: #while curr is not NULL
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
