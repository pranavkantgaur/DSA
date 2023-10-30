# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_subll(self, slow, fast):
        prev = None
        head = slow
        while(head != fast):
            k = head.next
            head.next = prev
            head = k
            prev = head
        return


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        last_ll_tail = None
        slow = head
        fast = head
        new_head = None
        while(fast):
            # create sliding window
            index = 0
            while(index < k - 1 and fast != None):
                fast = fast.next
                index += 1
            if fast == None:
                last_ll_tail.next = slow
                break
            # reverse ll within sliding window
            if new_head == None:
                new_head = fast
                next_ll_head = fast.next
            self.reverse_subll(slow, fast)        
            if last_ll_tail != None:
                last_ll_tail.next = fast
            # move the sliding window
            last_ll_tail = slow        
            slow = next_ll_head
            fast = slow
        return new_head    
               
        
