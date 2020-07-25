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
