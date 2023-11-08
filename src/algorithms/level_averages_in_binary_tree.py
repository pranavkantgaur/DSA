# Given a binary tree, populate an array to represent the averages of all of its levels.
#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def findLevelAverages(self, root):
    result = []
    queue = []
    queue.append(root)
    while(len(queue)):
      level_size = len(queue)
      current_sum = 0.0
      for _ in range(level_size):
        node = queue.pop(0)
        current_sum += node.val
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      result.append(current_sum / level_size)
    return result
