# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def heightOfTree(root):
    return 1 + max(heightOfTree(root.left), heightOfTree(root.right))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if isBalanced(root.left) and isBalanced(root.right):
            if abs(heightOfTree(root.left) - heightOfTree(root.right)) <= 1 :
                return True
            else:
                return False
        
