# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLinkedListCycleLength(self, head):
        # reach inside cycle
        fast = head
        slow = head
        while(fast and fast.next):#(fast != slow):
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break        
        if fast.next == None: # no cycle found.
            return -1
        # if the cycle is found.
        k = 1
        temp_node = slow
        while(temp_node.next != slow): # count the length of cycle
            k+=1
            temp_node = temp_node.next
        # increment the counter untill fast = slow again
        return k

    def getKthNodeFromPointer(self, node, k):
        count = 0
        while(count < k):
            node = node.next
            count += 1
        return node      


    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #TODO Write your code here
        k = self.getLinkedListCycleLength(head)
        if k == -1:
            return None
        slow = head
        fast = self.getKthNodeFromPointer(head, k)
        while(fast != slow):
            slow = slow.next
            fast = self.getKthNodeFromPointer(slow, k)
        return slow
        
