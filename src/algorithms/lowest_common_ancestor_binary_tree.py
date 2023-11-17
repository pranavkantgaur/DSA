# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkNodeExists(self, node, root):
        if root is None:
            return False
        if root.val == node.val:
            return True
        return self.checkNodeExists(node, root.left) or self.checkNodeExists(node, root.right)

    def getLCAHelper(self, p, q, root):
	    if root is None: return None
	    # check if either the p,q exist on either side of tree rooted at root or only p or q exists in one of the subtree
	    if self.checkNodeExists(p, root.left) != self.checkNodeExists(q, root.left) or self.checkNodeExists(p, root.right) != self. checkNodeExists(q, root.right): # present on one side only
		    return root
	    else:
		    lca_node = self.getLCAHelper(p, q, root.left)	    
		    if lca_node is None:
			    lca_node = self.getLCAHelper(p, q, root.right)
			    if lca_node is None:
				    return None
		    return lca_node		

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
	    return self.getLCAHelper(p, q, root) # return the LCA
