# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.issym(root.left,root.right)
        
    def issym(self, a, b):
        if not a and not b: return True
        if a and b and a.val == b.val: return self.issym(a.left,b.right) and self.issym(a.right,b.left)
        return False