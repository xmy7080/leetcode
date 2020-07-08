#https://leetcode.com/articles/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(a: TreeNode, b: TreeNode) -> bool:
            # print("in dfs, s is" + str(s.val))
            # print("in dfs, t is" + str(t.val))
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return dfs(a.left, b.left) and dfs(a.right, b.right)
        if not s:
            return False
        if dfs(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
