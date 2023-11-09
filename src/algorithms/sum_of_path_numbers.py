# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.
#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def getSum(self, current_path):
    total_sum = 0
    for id in range(len(current_path)):
      total_sum += current_path[id] * pow(10, len(current_path) - id - 1)
    return total_sum

  def helper(self, root, current_path):
    if root is None:
      return 0
    current_path.append(root.val)
    if root.left is None and root.right  is None:
      total_sum = self.getSum(current_path)
      del current_path[-1]
      return total_sum
    else:      
      sum1 = self.helper(root.left, current_path)
      sum2 = self.helper(root.right, current_path)
      del current_path[-1]
      return sum1 + sum2

  def findSumOfPathNumbers(self, root):
    total_sum = 0
    current_path = []
    total_sum = self.helper(root, current_path)
    return total_sum
