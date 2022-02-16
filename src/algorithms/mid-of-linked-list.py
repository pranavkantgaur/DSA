# Definition for singly-linked list.
# https://leetcode.com/problems/middle-of-the-linked-list/
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Approach - 1:
        1. Count number of nodes, n
        2. if n is even:
           2.1. return second middle node
        3. if n is odd:
            return middle node        
        
        temp = head
        n = 0
        while(temp):
          n += 1
        if n mod 2:
            target = n // 2
        else:
            target = n / 2 + 1
        index = 1
        temp  = head
        while(index < target):
            temp  = temp.next           
            
        Approach - 2:
        1. Set slow = head, fast ptr=head.next.next
        while fast.next :
          slow = slow.next
          fast = 2 * slow //how to do this? fast pointer must move 2 times faster than slow pointer
        
            
        '''
        
