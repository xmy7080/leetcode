# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isbst(root,sys.maxint * -1,sys.maxint)
        
    def isbst(self,node, min,max):
        if not node: return True
        if node.val<=min or node.val >= max: return False
        return self.isbst(node.left,min,node.val) and self.isbst(node.right,node.val,max)