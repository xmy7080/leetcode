#pony ai phone interview, lt 889
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) != len(post) or pre[0] != post[-1]:
            return None
        if pre == post:
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        pre = pre[1:]
        post = post[:-1]
        if pre[0] == post[-1]:
            root.left = self.constructFromPrePost(pre, post)
        else:
            lroot, rroot = pre[0], post[-1]
            # T     E
            lpre = pre[:pre.index(rroot) ]
            #'tcd'
            lpost = post[: post.index(lroot)+1]
            # ''
            root.left = self.constructFromPrePost(lpre, lpost)

            rpre = pre[pre.index(rroot):]
            rpost = post[post.index(lroot)+1:]
            root.right = self.constructFromPrePost(rpre, rpost)
            if not root.left or not root.right:
                return None
        return root
