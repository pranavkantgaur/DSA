# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
2-pass approach:
1. Compute length of list by iterating on all elements
2. If length > n:
   2.1. Reach n+1 element from last and remove nth node:
        node_to_be_deleted = node.next
        node.next = node_to_be_deleted.next
        delete node_to_be_deleted
1-pass approach:
1. Maintain a slow pointer, fast pointer
2. Difference in position of slow and fast pointerw will be n
3. Once fast pointer reaches the end, delete slow.next node
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # compute length of list
        length = 1
        node = head
        while node.next is not None:
            node = node.next
            length += 1
        # locate predecessor of the node to be deleted
        current_node_id = 1
        node = head
        while(current_node_id < length - n):
            node = node.next
        # delete the node
        node_to_be_deleted = node.next
        node.next = node_to_be_deleted.next
        del node_to_be_deleted
        
        # return head
        return head
        
