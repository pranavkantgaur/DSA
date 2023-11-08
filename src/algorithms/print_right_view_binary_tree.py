# Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def traverse(self, root):
    result = [] # List[int]
    queue = []
    queue.append(root)
    while(len(queue)):
      level_size = len(queue)
      for _ in range(level_size):
        node = queue.pop(0)
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      result.append(node.val)
    return result
