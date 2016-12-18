# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)
        
    def helper(self,node):
        if not node: return 0
        leftdepth = self.helper(node.left)
        rightdepth = self.helper(node.right)
        return 1 + (leftdepth if leftdepth > rightdepth else rightdepth)