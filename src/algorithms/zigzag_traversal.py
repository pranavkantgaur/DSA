# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same manner for the following levels. 
#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def traverse(self, root):
    result = []
    queue = []
    current_level = []
    queue.append(root)
    level_id = 1
    while(len(queue)):
      level_size = len(queue)
      for _ in range(level_size):
        node = queue.pop(0)
        if level_id % 2 == 0:
          current_level.insert(0, node.val)
        else:
          current_level.append(node.val)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      result.append(current_level)
      current_level = []
      level_id += 1
    return result
