#down top dfs solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def helper(node) -> (int, int):
            leftL, leftH = helper(node.left) if node.left else (None, None)
            rightL, rightH = helper(node.right) if node.right else (None,None)
            low = node.val
            high = node.val
            if node.left:
                low = min(low, leftL)
                high = max(high, leftH)
            if node.right:
                low = min(low, rightL)
                high = max(high, rightH)
            # print("node val is " + str(node.val))
            # print("min is " + str(low))
            # print("max is " + str(high))
            self.ans = max(abs(node.val - low), abs(node.val - high), self.ans )
            # print("ans is " + str(self.ans))
            return (low, high)
        helper(root)
        return self.ans
