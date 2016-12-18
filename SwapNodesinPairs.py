# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head
        a, b = h, head
        if not b: return head
        c = b.next
        if not c: return head
        d = c.next
        
        while c:
            a.next = c
            b.next = d
            c.next = b
            if d and d.next:
                a = b
                b = d
                c = d.next
                d = d.next.next
            else:
                break
        return h.next