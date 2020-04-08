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
        #======
        #recent approach
        if not root: return None
        p_val, q_val = sorted([p.val, q.val])
        # print("\n p val is "+str(p.val) + " q val is "+ str(q.val))
        # print("\n root val is "+str(root.val) )
        if p_val <= root.val <= q_val:
            return root
        elif p_val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif q_val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return None
            
            
        
        
        
        
        
        
        
        
        # (a,b) = sorted([p.val,q.val])
        # while not a <= root.val <= b:
        #     root = (root.left,root.right)[a>root.val]
        # return root
