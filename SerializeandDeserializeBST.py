# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def preorder(node):
            if node:
                vals.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ' '.join(map(str,vals))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dq = collections.deque(int(val) for val in data.split())
        def buildtree(min, max):
            if dq and min<dq[0]<max:
                v = dq.popleft()
                node = TreeNode(v)
                node.left = buildtree(min, v)
                node.right = buildtree(v,max)
                return node
        return buildtree(float('-infinity'),float('infinity'))
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))