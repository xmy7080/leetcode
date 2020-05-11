#lt solution with dfs and delimiter '#'
#https://leetcode.com/articles/serialize-and-deserialize-n-ary-tree/
#chr(val + 48) is because we using '#' as delimiter, because ord('#') is 35, so we want the ord at least start from 36
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        ls = []
        self._serializeList(root, ls)
        return "".join(ls)
        
    def _serializeList(self, node, ls):
        if not node:
            return
        ls.append(chr(node.val + 48) )
        for child in node.children:
            self._serializeList(child, ls)
        ls.append('#')
	
    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        self.index = 0
        return self._deserializeHelper(data)
    
    def _deserializeHelper(self, data):
        if self.index == len(data):
            return None
        
        node = Node(ord(data[self.index]) - 48, [] )
        self.index += 1
        while data[self.index] != '#':
            node.children.append(self._deserializeHelper(data) )
        
        self.index += 1
        return node
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
