#leetcode iterative solution, super easy to pick up
#https://leetcode.com/articles/flatten-a-multilevel-doubly-linked-list/
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        dummyH = Node(None, None, head, None)
        prev = dummyH
        
        stack = []
        stack.append(head)
        
        while stack:
            curr = stack.pop()
            
            curr.prev = prev
            prev.next = curr
            
            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        dummyH.next.prev = None
        return dummyH.next
