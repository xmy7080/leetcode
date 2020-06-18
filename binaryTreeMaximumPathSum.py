#consider 4 different cases, left+node.val, right + node.val, left+right+node.val, node.val itself. 
#all could be the new max
#also when return the curr max, we should only consider one path to the left or right, or just the curr node itself.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float('inf')
        def dfs(node) -> int:
            # if not node:
            #     return None
            left  = 0 if not node.left  else dfs(node.left)
            right = 0 if not node.right else dfs(node.right)
            val = node.val
            self.ans = max(left+val, right + val, left+right+val, val, self.ans)
            return max(left+val, right + val, val)
        dfs(root)
        return self.ans
