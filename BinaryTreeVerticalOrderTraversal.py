# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        rlist = []#vertical place of[0,1,2,3,...]
        llist = []#vertical place of[-1,-2,-3...]
        q = collections.deque()
        q.append((0,root))
        while q:
            posi, node = q.popleft()
            self.helper(posi,node,rlist,llist)
            if node.left:
                q.append((posi-1,node.left))
            if node.right:
                q.append((posi+1,node.right))
        llist.reverse()
        return llist+rlist
        
    def helper(self,posi,node,rlist,llist):
        if not node: return
        if posi >=0: 
            if posi < len(rlist):#if position is within the span of list,take sublist out and insert n
                tmpl = rlist.pop(posi)
                tmpl.append(node.val)
                rlist.insert(posi,tmpl)
            else:#if position is out of bound of list, append new sublist to list
                tmpl = [node.val]
                rlist.append(tmpl)
        else:
            posi = -posi
            if posi-1 < len(llist):
                tmpl = llist.pop(posi-1)
                tmpl.append(node.val)
                llist.insert(posi-1,tmpl)
            else:
                tmpl = [node.val]
                llist.append(tmpl)
            posi = -posi
        