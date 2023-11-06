# Given the head node of a singly linked list, modify the list such that any node that has a node with a greater value to its right gets removed. The function should return the head of the modified list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head):
        '''
        1. The monotonic decreasing stack will have nodes in the same order as on resulting linked list
        2. Pop nodes from the stack untill the value of top element is greater than that of the current node
        3. If this results in emptying of the stack, update the head.
        '''
        current = head
        stack = []
        while(current):
          while(stack and current.val > stack[-1].val):
            stack.pop(-1)
          if stack:
            stack[-1].next = current
          else:
            head = current            
          stack.append(current)
          current = current.next

        return head
