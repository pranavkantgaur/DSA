# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and not head.next:
            return None
        slow = head
        fast = head
        count = n
        while(count > 0):
            fast = fast.next
            count -= 1
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next
        
        node_to_be_deleted = slow.next
        slow.next = slow.next.next     
        return head
