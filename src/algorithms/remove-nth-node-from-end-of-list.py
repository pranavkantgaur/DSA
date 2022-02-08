# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
# edge cases:
1. n = length
2. n = 1
3. length = 1


# 2-pass approach:
1. Compute length of list by iterating on all elements
2. If length > n:
   2.1. Reach n+1 element from last and remove nth node:
        node_to_be_deleted = node.next
        node.next = node_to_be_deleted.next
        delete node_to_be_deleted


# 1-pass approach:
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
        # check for edge-cases
        if length == n:
            node_to_be_deleted = head
            head = head.next
            del node_to_be_deleted
            return head        
        # locate predecessor of the node to be deleted
        current_node_id = 1
        node = head
        while(current_node_id < length - n):
            node = node.next
            current_node_id += 1
        # delete the node
        node_to_be_deleted = node.next
        node.next = node_to_be_deleted.next
        del node_to_be_deleted
        
        # return head
        return head
    
    # todo: CHECK FOR head = [1,2,3,4,5], n = 2
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # initialize slow and fast pointers
        slow = head
        fast = head
        
        # inflate slow-fast window from one end, by moving fast pointer and keeping slow pointer fixed
        node_id = 1
        while(node_id < n):
            fast = fast.next
            node_id += 1
            
        # move the slow-fast window, untill fast does not reach the tail of the linked list
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        # once fast pointer is at the tail of the linked list, remove slow.next node
        node_to_be_deleted = slow.next
        slow.next = node_to_be_deleted.next
        del node_to_be_deleted
        
        # return head
        return head
