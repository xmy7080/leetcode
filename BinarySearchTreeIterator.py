# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stk = []
        while root:
            self.stk.append(root)
            root = root.left

    def hasNext(self):
        return self.stk
        

    def next(self):
        curr = self.stk.pop()
        val = curr.val
        curr = curr.right
        while curr:
            self.stk.append(curr)
            curr = curr.left
        return val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())