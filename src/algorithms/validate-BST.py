# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMaxValueBST(self, bst_root):
        pass
    def getMinValueBST(self, bst_root):
        pass
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.isValidBST(root.left) and self.isValidBST(root.right) 
            if self.getMaxValueBST(root.left) < root.key and self.getMinValueBST(root.right) > root.key:
                return True
            else:
                return False
        else:
            return False
            
        
