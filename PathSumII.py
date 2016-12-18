# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:return []
        tmp = []
        self.ps(tmp,root,sum)
        return self.res
        
    def ps(self,tmp,node,sum):
        if not node: return
        if not node.left and not node.right and sum == node.val:
            tmp.append(node.val)
            ist = list(tmp)
            self.res.append(ist)
            del tmp[-1:]
            return
        tmp.append(node.val)
        if node.left:
            self.ps(tmp,node.left,sum-node.val)
        if node.right:
            self.ps(tmp,node.right,sum-node.val)
        del tmp[-1:]