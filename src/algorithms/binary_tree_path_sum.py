# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def hasPath(self, root, sum):
    if root is None:
      return False
    if root.val == sum and root.left is None and root.right is None:
        return True
    if root.left and self.hasPath(root.left, sum - root.val):
      return True
    if root.right and self.hasPath(root.right, sum - root.val):
      return True      
    return False
