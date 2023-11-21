# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def containsNode(root, node):
            if root is None: return False
            if root == node: return True
            return containsNode(root.left, node) or containsNode(root.right, node)

        if root in [p, q]: return root    
        contains_p = containsNode(root.left, p)
        contains_q = containsNode(root.left, q) 
        if contains_p != contains_q: return root
        # wither left contains both nodes or it contains None    
        if contains_p:
            return self.lowestCommonAncestor(root.left, p, q)     
        else:
            return self.lowestCommonAncestor(root.right, p, q) # p, q are in root.right subtree
