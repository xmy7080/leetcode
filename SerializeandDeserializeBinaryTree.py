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
        s = ""
        if not root:
            s += "null,"
        else:
            s += str(root.val) + ","
            s += self.serialize(root.left)
            s += self.serialize(root.right)
        return s
    
    #this is un used.
#     def buildstring(self,node,s):
#         if not node:
#             s += "null,"
#         else:
#             s += str(node.val) + ","
#             self.buildstring(node.left,s)
#             self.buildstring(node.right,s)
#         return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(",")
        
        return self.buildtree(lst)
        
    def buildtree(self, lst):
        s = lst.pop(0)
        if s == "null" or s == "":
            return None
        else:
            node = TreeNode(int(s))
            node.left = self.buildtree(lst)
            node.right = self.buildtree(lst)
            return node
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
