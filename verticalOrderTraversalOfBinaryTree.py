#in this question the order of the vertical does matter, hence we need bfs way
#also when two node is at the same position, we order the smaller one ahead
#use deque and a tmp list, sort the list by its val when x position is the same
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        leftmost, rightmost = 0, 0
        que = collections.deque()
        tmpq = []
        vertical = collections.defaultdict(list)
        que.append((0, root) )
        
        while que:
            x ,node = que.popleft()
            vertical[x].append(node.val)
            if node.left:
                leftmost = min(leftmost, x-1)
                tmpq.append((x-1, node.left))
            if node.right:
                rightmost = max(rightmost, x+1)
                tmpq.append((x+1, node.right))
            if not que and tmpq:
                que = collections.deque(sorted(tmpq, key = lambda x: (x[0], x[1].val) ))
                tmpq = []
        ans = []
        for k in range(leftmost, rightmost+1):
            ans.append(vertical[k])
        return ans
        # self.leftmost = 0
        # self.rightmost = 0
        # vertical = collections.defaultdict(list)
        # def bfs(node, x):
        #     if not node:
        #         return
        #     vertical[x].append(node.val)
        #     self.leftmost = min(self.leftmost, x)
        #     self.rightmost = max(self.rightmost, x)
        #     bfs(node.left, x -1)
        #     bfs(node.right, x +1)
        # bfs(root, 0)
        # ans = []
        # for k in range(self.leftmost, self.rightmost+1):
        #     ans.append(vertical[k])
        # return ans
