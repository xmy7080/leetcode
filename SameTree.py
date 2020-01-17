# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q: return True
        if p and q and p.val==q.val: return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
    
    
#======2020 prepare====
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
        if root == None:
            return True
        return self.helper(root.left, root.right)
        
        
    def helper(self, t1, t2):
        if t1 != None and t2 != None:
            return t1.val == t2.val and self.helper(t1.left, t2.right) and self.helper(t1.right, t2.left)
        elif t1 == None and t2 == None:
            return True
        return False
        
