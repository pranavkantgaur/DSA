# Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def findDepth(self, root):
    if not root:
      return 0
    minimumTreeDepth = 1
    queue = []
    queue.append(root)
    while(len(queue)):
      level_size = len(queue)
      for _ in range(level_size):
        node = queue.pop(0)
        if node.left is None and node.right is None: # leaf node
          return minimumTreeDepth
        else:
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)
          minimumTreeDepth += 1

