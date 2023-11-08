# Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None


class Solution:
  def findSuccessor(self, root, key):
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
        if node.val == key:
          if len(queue):
            return queue.pop(0)
          else:
            return None
