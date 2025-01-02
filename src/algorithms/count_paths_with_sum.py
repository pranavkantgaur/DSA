#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right
class Solution:  
    def _get_path_count(self, prefix_sum, S): 
        count = 0
        for i in range(len(prefix_sum) - 1):
            if prefix_sum[-1] - prefix_sum[i] == S: 
                count += 1  
        if prefix_sum[-1] == S: count += 1 
        return count  

    def dfs_recur(self, root, S, prefix_sum): 
        if root == None:
            return 0
        if prefix_sum:
            prefix_sum.append(prefix_sum[-1] + root.val) 
        else:
            prefix_sum.append(root.val) 
        count = self._get_path_count(prefix_sum, S) 
        count += self.dfs_recur(root.left, S, prefix_sum) 
        count += self.dfs_recur(root.right, S, prefix_sum) 
        prefix_sum.pop()
        return count 

    def countPaths(self, root, S):  
        prefix_sum = []
        return self.dfs_recur(root, S, prefix_sum)  
