# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        a, b = sorted([p.val,q.val])
        while not a<= root.val <= b:
            if b<root.val:
                root = root.left
            if a>root.val:
                root = root.right
        return root
            
            
            
        
        
        
        
        
        
        
        
        # (a,b) = sorted([p.val,q.val])
        # while not a <= root.val <= b:
        #     root = (root.left,root.right)[a>root.val]
        # return root