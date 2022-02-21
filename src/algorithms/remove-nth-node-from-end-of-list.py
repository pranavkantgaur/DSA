# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # todo: CHECK FOR head = [1,2], n = 2
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and not head.next:
            return None
        slow = head
        fast = head
        count = n
        while(count > 0):
            fast = fast.next
            count -= 1
        if not fast: # means we want to delete the head node (Does it always hold?)
            head = head.next
            return head
         while(fast.next):
            slow = slow.next
            fast = fast.next
            
        node_to_be_deleted = slow.next
        slow.next = slow.next.next     
        return head
