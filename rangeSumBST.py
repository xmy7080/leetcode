# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root: return 0
        base = root.val if L <= root.val and R >= root.val else 0
        if root.val >= R: #if root is on the right side of range, ignore right subtree
            return base + self.rangeSumBST(root.left, L, R) 
        if root.val <= L: #if root is on the left side of range, ignore left subtree
            return base + self.rangeSumBST(root.right, L, R) 
        #don't ignore subtree if root fall in range
        return base + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) 
