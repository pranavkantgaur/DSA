# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in [p, q]: return root
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        if min_val < root.val < max_val: return root    
        if min_val > root.val: return self.lowestCommonAncestor(root.right, p, q)
        if max_val < root.val: return self.lowestCommonAncestor(root.left, p, q)
