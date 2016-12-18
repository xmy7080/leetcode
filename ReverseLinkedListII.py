# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n: return head
        h = ListNode(0)
        h.next = head
        p,q,s,i = h,head,head.next,1
        before = None
        while p:
            if i == m:
                before = p
            elif i>m and i<=n:
                q.next = p
            elif i == n+1:
                before.next.next = q
                before.next = p
                break
            p,q = q,s
            if s: s = s.next
            
            i += 1
        return h.next