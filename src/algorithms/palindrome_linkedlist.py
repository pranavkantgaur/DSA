# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TC: O(n), SC: O(1)
class Solution:
    def getMidNode(self, head):
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow            

    def getReversedLL(self, head, last_node):
        prev_node = None
        current_node = head
        while(current_node != last_node):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node # return head of reversed ll            

    def getLLLength(self, head):
        node = head
        length = 0
        while(node != None):            
            length += 1
            node = node.next
        return length + 1            


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        1. Mid of ll
        2. Reverse ll from start to mid - 1, l1
        3. Compare l1, l2, update boolean flag
        4. Restore ll
        5. Return flag
        '''
        mid_node = self.getMidNode(head)         
        ll_length = self.getLLLength(head)
        if ll_length % 2 == 0:
            l2 = mid_node.next            
        else:
            l2 = mid_node
            
        reversed_ll_head = self.getReversedLL(head, l2)                    
        l1 = reversed_ll_head        
        while(l1 and l2 and l1.val == l2.val):
            l1 = l1.next
            l2 = l2.next
        if not l1 and not l2:
            is_palindrome = True
        else:
            is_palindrome = False
        head = self.getReversedLL(reversed_ll_head, None)                                   
        reversed_ll_head.next = l2
        return is_palindrome

        
