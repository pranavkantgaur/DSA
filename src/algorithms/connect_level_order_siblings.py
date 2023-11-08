# Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = self.right = self.next = None

class Solution:
    def connect(self, root):
        queue = []
        queue.append(root)
        while(len(queue)):
          level_size = len(queue)
          for id in range(level_size):
            node = queue.pop(0)
            if id < level_size - 1:
              node.next = queue[0]
            else:
              node.next = None
            if node.left:
              queue.append(node.left)
            if node.right:
              queue.append(node.right)
        return root

