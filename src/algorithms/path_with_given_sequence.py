# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPath(self, root, sequence):
    if root is None: 
      return len(sequence) == 0
    if root.val == sequence[0]:
      if len(sequence) == 1:
        if root.left is None and root.right is None: # leaf
          return True
        else:
          return False
      else:
        return self.findPath(root.left, sequence[1:]) or self.findPath(root.right, sequence[1:])
    else:
      return False
