# Given the head node of a singly linked list, modify the list such that any node that has a node with a greater value to its right gets removed. The function should return the head of the modified list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head):
        # push nodes to the monotonic decreasing stack along with their prev node address
        # if a node with higher value if found, for each popped node from the stack, delete it from linked list
        # make sure to set prev, head pointers correctly after deleting the node from ll 
        # we are updating the linked list in the same loop we are iterating on it.
        prev = None
        current = head
        stack = [] # <node, prev_node>
        while(current):          
          while(len(stack) > 0  and current.val > stack[-1][0].val):
            top_node, top_prev_node = stack.pop(-1)                      
            if top_prev_node:
              # delete the node
              top_prev_node.next = current
              prev = top_prev_node
            else:
              head = current 
              prev = None           
            del top_node            

          stack.append([current, prev])
          prev = current
          current = current.next
        
        return head
