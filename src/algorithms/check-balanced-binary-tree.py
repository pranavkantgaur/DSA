# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def heightOfTree(self, root):
        if not root:
            return -1
        return 1 + max(self.heightOfTree(root.left), self.heightOfTree(root.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root: # 0
            if self.isBalanced(root.left) and self.isBalanced(root.right): # 4 4
                if abs(self.heightOfTree(root.left) - self.heightOfTree(root.right)) <= 1 :
                    return True
                else:
                    return False
            else:
                return False
        else:
            return True
                        
