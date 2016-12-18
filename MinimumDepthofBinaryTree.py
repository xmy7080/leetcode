# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)
        
    def helper(self,node):
        if not node: return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        if left == 0:return right + 1
        if right == 0:return left + 1
        return 1 + (left if left < right else right)