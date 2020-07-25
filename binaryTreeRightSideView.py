#lt solution at https://leetcode.com/articles/binary-tree-right-side-view/
Time complexity is the same O N both for DFS and BFS since one has to visit all nodes.

Space complexity is O(H) for DFS and
O(D) for BFS, where H is a tree height, and D is a tree diameter. 
They both result in O(N) space in the worst-case scenarios: skewed tree for DFS and complete tree for BFS.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(res, root, 0)
        return res
        
    def helper(self, res, node, level):
        if not node:
            return
        if node and level == len(res):
            res.append(node.val)
        self.helper(res, node.right, level+1)
        self.helper(res, node.left, level+1)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        que = collections.deque()
        tmpq = collections.deque()
        que.append(root)
        res = [root.val]
        while que:
            node = que.popleft()
            if node.left:
                tmpq.append(node.left)
            if node.right:
                tmpq.append(node.right)
            
            if tmpq and not que:
                res.append(tmpq[len(tmpq)-1].val )
                que = tmpq.copy()
                tmpq = collections.deque()
        return res
