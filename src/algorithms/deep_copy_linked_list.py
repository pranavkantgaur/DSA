'''
https://leetcode.com/problems/copy-list-with-random-pointer/description/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create and attahch duplicate nodes to original list
        if head is None:
            return None
        o_node = head    
        while(o_node):
            temp = o_node.next
            d_node = Node(o_node.val)
            o_node.next = d_node
            d_node.next = temp
            o_node = temp
    	    # set random ptr for d_nodes
        o_node = head
        head_d = o_node.next
        while(o_node):
            d_node = o_node.next
            if o_node.random:
                d_node.random = o_node.random.next
            o_node = d_node.next
	    # detach the lists, restore the o_node next ptrs and set d_node nexts	
        o_node = head
        while(o_node):
            d_node = o_node.next
            o_node.next = d_node.next
            if d_node.next:
                d_node.next = d_node.next.next
            o_node = o_node.next

        return head_d	

