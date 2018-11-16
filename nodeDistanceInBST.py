import collections
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# nodes = [2,5,6,8,10,1]

# nodes = [8,10,6,2,5,1]

# nodes = [6,5,2,1,10,8]

# nodes = [6,2,10,1,5,8]

nodes = [1,2,5,6,8,10]
a, b = 2, 8

def add(root, v):
    if not root:
        root = TreeNode(v)
    elif root.val > v:#left subtree
        root.left = add(root.left, v)
    else:
        root.right = add(root.right, v)
    return root

def path(root, v, pat):
    pat.append(root.val)
    if root.val == v:
        return pat
    else:
        if root.val < v: #down right
            return path(root.right, v, pat)
        else:
            return path(root.left, v, pat)
        
def nodeDistanceInBST(nodes, a, b):
    root = None
    for n in nodes:
        root = add(root, n)
    pat1 = path(root, a, [])
    pat2 = path(root, b, [])
    i = 0
    while i< len(pat1) and i< len(pat2):
        if pat1[i] == pat2[i]: i += 1
        else: break
    return (len(pat1) + len(pat2) - 2* i)
    
print (nodeDistanceInBST(nodes, a, b))
