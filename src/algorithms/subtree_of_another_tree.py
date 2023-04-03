# https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val == subRoot.val:
            if self.isSubtree(root.left, subRoot.left) and isSubtree(root.right, subRoot.right):
                return True
            else:
                if self.isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot):                 
                    return True
                else:
                    return False
        else:
            if self.isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot):                 
                return True
            else:
                return False
