#binary search way and only using while loop
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
        #my clumsy solution
        # def deeper(node: TreeNode) -> int:
        #     res = node.val
        #     if node.left and node.val > target:
        #         subclose = deeper(node.left)
        #         if abs(res - target) > abs(subclose - target):
        #             res = subclose
        #     if node.right and node.val < target:
        #         subclose = deeper(node.right)
        #         if abs(res - target) > abs(subclose - target):
        #             res = subclose
        #     return res
        # return deeper(root)
