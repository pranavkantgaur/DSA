# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def traverse(self, root):
    queue = []
    queue.append(root)  
    current_level = []
    result = []
    while(len(queue)):
      level_size = len(queue)
      for _ in range(level_size):
        node = queue.pop(0)
        current_level.append(node.val)     
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      result.append(current_level)        
      current_level = []
    return result        
