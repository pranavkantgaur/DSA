#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right, self.next = None, None, None


class Solution:
  def connect(self, root):
    queue = []
    queue.append(root)
    prev = None 
    while(len(queue)):
      level_size = len(queue) # do not reset prev to None so that nodes across successive levels are also connected.
      for _ in range(level_size):
        current = queue.pop(0)
        if prev:
          prev.next = current
        prev = current
        if current.left:
          queue.append(current.left)
        if current.right:
          queue.append(current.right)
    return root

