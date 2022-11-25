# https://leetcode.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        first = head
        last = get_last_node()
        penultimate = get_penultimate_node()
        if first is None: # no element in list
            return
        if first == last: # 1 element in list
            return first            
        if first == penultimate: # 2 elements in list
            return
        else: # more than 2 elements in the list
            t = first.next
            first.next = last
            last.next = t.next
            penultimate.next = None            
            reorderList(first.next.next)            
            return 
