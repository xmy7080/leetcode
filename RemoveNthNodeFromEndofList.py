# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #check input
        if not head or not n:
            return head
        #initial p and q
        newhead = ListNode(0)
        newhead.next = head
        p = newhead
        q = p
        while n >0 :#move the q to the n next of p
            if q.next:
                q = q.next
            else:
                return head
            n -= 1
        while q.next:#move both downward till q hit last un None
            p = p.next
            q = q.next
        p.next = p.next.next
        return newhead.next
        