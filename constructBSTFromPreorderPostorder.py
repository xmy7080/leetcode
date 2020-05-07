#pony ai phone interview, lt 889
#lt concise solution
class Solution(object):
    def constructFromPrePost(self, pre, post):
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root
#my actual answer during interview
"""

Given  2 strings:
pre-order:  ABCDE
post-order: CDBEA

illustration:
     A
    / \
    B  E
   / \ /\
   C D F G

    A
   / \
     B
    /\
    C D

A B CD
CD B A
1. Construct a binary tree satisfying the two conditions?
a b cd e fg
cdb fg e a

b c d
c d b
"""
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
