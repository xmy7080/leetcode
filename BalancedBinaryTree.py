# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.isbal = True
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        self.helper(root)
        return self.isbal
    
    def helper(self,node):
        if not node: return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        if abs(left - right) > 1: self.isbal = False
        return 1 + (left if left>right else right)