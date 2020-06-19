#lt solution, two cases discussion
#iterative in order traverse under the second case
#https://leetcode.com/articles/inorder-successor-in-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        #p has right sub tree, go to leftmost node in that
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        #p doesn't have right subtree
        stk, prev = [], float('inf')
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            #pop stk, which is the leftmost node so far
            root = stk.pop()
            if prev == p.val:
                return root
            prev = root.val
            
            root = root.right
            
