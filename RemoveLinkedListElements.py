# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return head
        h = ListNode(-1)
        h.next = head
        n = h
        while n.next:
            if n.next.val == val:
                p = n.next
                while p:
                    if p.val != val:break
                    p = p.next
                if p:
                    n.next.val = p.val
                    n.next.next = p.next
                else:
                    n.next = None
                    break
            n = n.next
        return h.next