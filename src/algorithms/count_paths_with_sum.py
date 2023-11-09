# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def getCountOfSubpathWithCurrentEndSum(self, target_sum, current_path):
    # keep last index fixed and check if there is a subarray with last id = -1 with sum = target_sum
    cum_sum = current_path[-1]
    i = 2
    while(cum_sum < target_sum and i <= len(current_path)): # assuming all values to be > 0
      cum_sum += current_path[-i]
      i += 1
    if cum_sum == target_sum:
      return 1
    else:
      return 0

  def helper(self, root, target_sum, current_path):
    if root is None:
      return 0
    current_path.append(root.val)    
    count0 = self.getCountOfSubpathWithCurrentEndSum(target_sum, current_path)
    count1 = self.helper(root.left, target_sum, current_path)
    count2 = self.helper(root.right, target_sum, current_path)
    del current_path[-1]
    return count0 + count1 + count2
  
  def countPaths(self, root, S):
    '''
    for each newly visited node, check how many subpaths(or subarrays in current_path) sum to S
    '''
    current_path = []
    path_count = self.helper(root, S, current_path)
    return path_count
