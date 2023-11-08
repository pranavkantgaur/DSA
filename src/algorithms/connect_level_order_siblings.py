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
        prev = None
        for _ in range(level_size):
          current = queue.pop(0)
          if prev:
            prev.next = current         
          prev = current  
          current.next = None
          if current.left:
            queue.append(current.left)
          if current.right:
            queue.append(current.right)
      return root

