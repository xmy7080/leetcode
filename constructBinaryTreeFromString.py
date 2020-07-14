#lc solution
#https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100422/Python-Straightforward-with-Explanation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        lidx = s.find('(')
        if lidx <0:
            return TreeNode(int(s) ) if s else None
        count = 0
        for ridx, u in enumerate(s):
            if u == ')': count -= 1
            if u == '(': count += 1
            if ridx > lidx and not count:
                break
        
        node = TreeNode(int(s[:lidx]) )
        node.left = self.str2tree(s[lidx+1: ridx])
        node.right = self.str2tree(s[ridx+2: -1])
        return node
