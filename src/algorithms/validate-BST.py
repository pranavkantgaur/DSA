# https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMaxValueBST(self, bst_root):
        '''
        return the value of the rightmost node in a BST
        '''
        node = bst_root
        while node.right:
            node = node.right
        return node.val                        
        
    def getMinValueBST(self, bst_root):
        '''
        return value of the leftmost node in a BST
        '''
        node = bst_root
        while node.left:
            node  = node.left
        return node.val            
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None: # leaf node
            return True

        if root.left is None and root.right: # node with right child only
            if self.isValidBST(root.right) and self.getMinValueBST(root.right) > root.val: 
                return True 
            else:
                return False
        if root.left and root.right is None: # node with left child only
            if self.isValidBST(root.left) and self.getMaxValueBST(root.left) < root.val: 
                return True
            else:
                return False
        # in other cases            
        if self.isValidBST(root.left) and self.isValidBST(root.right): # other cases
            if self.getMaxValueBST(root.left) < root.val and self.getMinValueBST(root.right) > root.val:
                return True
            else:
                return False
        else:
            return False
            
                    
        
