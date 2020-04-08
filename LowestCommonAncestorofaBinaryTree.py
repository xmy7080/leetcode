# leetcode solution
https://leetcode.com/articles/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if not node: return False
            left  = helper(node.left)
            right = helper(node.right)
            mid = node.val == p.val or node.val == q.val
            if mid + left + right > 1:
                self.ans = node
            return mid or left or right
        
        helper(root)
        return self.ans
        
#========
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left != None and right != None: return root
        return left if left else right
        
        
        
        
        
        
        
        
        
        
        
        
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # if root == None or root == p or root == q : return root
        # left = self.lowestCommonAncestor(root.left,p,q)
        # right = self.lowestCommonAncestor(root.right,p,q)
        # if left != None and right != None: return root
        # return (left,right)[not left]
