# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        #check input
        
        #new stack and push root in
        stk = []
        curr = root
        while curr:
            stk.append(curr)
            curr = curr.left
        while stk:
            #when out of inner while loop and stack not None,
            #curr = stack.pop()
            curr = stk.pop()
            res.append(curr.val)
            curr = curr.right
            while curr:
                stk.append(curr)
                curr = curr.left
        return res
        #put curr value in list
        
        #curr = curr.right
        
        #stack allow the last pushed ele out first, thus we push the root first, then traverse into
        #left, when there are no valid left, we pop up the stack to record the fresh pushed root node, then traverse in
        #right, same logic happends all over again
        # res = []
        # stk = []
        # node  = root
        # while stk or node:
        #     if node:
        #         stk.append(node)
        #         node = node.left
        #     elif stk:
        #         node = stk.pop()
        #         res.append(node.val)
        #         node = node.right
        # return res