# Definition for a binary tree node.
#leetcode solution #1 and #2
#https://leetcode.com/articles/maximum-product-of-splitted-binary-tree/
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = 0
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def totalSum(node):
            if not node: return 0
            return node.val + totalSum(node.left) + totalSum(node.right)
        self.ans = 0
        totalS = totalSum(root)
        def dfs(node):
            if not node: return 0
            leftS = dfs(node.left)
            rightS = dfs(node.right)
            nodeS = node.val + leftS + rightS
            product = nodeS * (totalS - nodeS)
            self.ans = max(self.ans, product)
            return nodeS
        
        dfs(root)
        return self.ans % (10 ** 9 + 7)
