# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr = l1
        l2_ptr = l2
        new_list_head = None
        carry_over = 0
        while l1_ptr and l2_ptr:
            if l1_ptr.val + l2_ptr.val + carry_over < 10:
                if new_list_head is None:
                    new_list_head = ListNode(l1_ptr.val + l2_ptr.val + carry_over)
                    new_list_ptr = new_list_head
                else:
                    new_list_ptr.next = ListNode(l1_ptr.val + l2_ptr.val + carry_over)
                    new_list_ptr = new_list_head
                    new_list_ptr = new_list_ptr.next
                new_list_ptr.next = None
                carry_over = 0
            else:
                if new_list_head is None:
                    new_list_head = ListNode(l1_ptr.val + l2_ptr.val + carry_over - 10)
                    new_list_ptr = new_list_head                   
                else:
                    new_list_ptr.next = ListNode(l1_ptr.val + l2_ptr.val + carry_over - 10)
                    new_list_ptr = new_list_ptr.next
                new_list_ptr.next = None                                
                carry_over = 1
            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next                
        while(l1_ptr):
            new_list_ptr.next = ListNode(l1_ptr.val)
            new_list_ptr = new_list_ptr.next
            new_list_ptr.next = None
            l1_ptr = l1_ptr.next                  
        while(l2_ptr):
            new_list_ptr.next = ListNode(l2_ptr.val)
            new_list_ptr = new_list_ptr.next
            new_list_ptr.next = None
            l2_ptr = l2_ptr.next                              
        return new_list_head            
