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
        return the value of the rightmost node
        '''
        node = bst_root
        while node.right:
            node = node.right
        return node.val                        
        
    def getMinValueBST(self, bst_root):
        '''
        return value of the leftmost node
        '''
        node = bst_root
        while node.left:
            node  = node.left
        return node.val            
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None: # left node
            return True
        '''
        if root.left is null and root.right is not null, check if root.right.key > root.key: true else false
        if root.left is not null and root.right is null, check if root.left.key < root.key: true else false
        '''
        if root.left is None and root.right:
            if root.right.val > root.val: 
                return True 
            else:
                return False
        if root.left and root.right is None:
            if root.left.val < root.val: 
                return True
            else:
                return False
        # in other cases            
        if self.isValidBST(root.left) and self.isValidBST(root.right): 
            if self.getMaxValueBST(root.left) < root.val and self.getMinValueBST(root.right) > root.val:
                return True
            else:
                return False
        else:
            return False
            
        
