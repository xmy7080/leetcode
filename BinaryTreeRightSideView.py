# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(res, root, 0)
        return res
        
    def helper(self, res, node, level):
        if not node:
            return
        if node and level == len(res):
            res.append(node.val)
        self.helper(res, node.right, level+1)
        self.helper(res, node.left, level+1)
        