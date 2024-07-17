'''
We are given the head of the list and we want to remove the nth node from the END of the list
we can think about reversing the list, but there is a easier way
We can use 2 pointers
L and R
Where do we place them
L and R should have a distacne of n, how 

n = 2
[1, 2, 3, 4, 5]
 L.    R
 So by the time R reaches the end
[1, 2, 3, 4, 5, NULL]
          L.     R
L will be at the node we want to delete 
But how we remove the node is simply update the .next of the previous node
we want 
1 -> 2 -> 3 -> 5 -> NULL, so we actually want our L to be one before 
and since we have to return the head of the list, we can initalize a dummy Node
the Dummy Node will go right before the head of the list, and left will be initalied there

so:
And R will still be shifted n times after the head, so by the time it reaches the end 
L will be at the previous node before the node we want to remove
Dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> NULL
 L                 R
                   L                R
then all we have to do is remove the link from 3 -> 4
and make the link 3 -> 5
just update L.next to L.next.next
and to return the head, jsut do dummy.next

Time: O(N) for 2 pointers and going thourhgh the input
Space: O(1), how much does it add to create a single listNode
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) #this makes head the .next of our dummy
        left = dummy
        right = head

        #this will put our R, n distance away from the node we wnat to remove
        while n > 0 and right: #while n is larger than 0, and right has not reached the end 
            right = right.next
            n -= 1 
        
        while right:
            left = left.next
            right = right.next
        
        #now left is at the node right before the node we want to remove
        left.next = left.next.next
        # just need to update the link, and the node is no longer in the list

        return dummy.next
        
