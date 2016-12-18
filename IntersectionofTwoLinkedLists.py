# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = self.length(headA)
        lb = self.length(headB)
        a = headA
        b = headB
        while la > lb:
            a = a.next
            la -= 1
        while lb > la:
            b = b.next
            lb -= 1
        while a != b:
            a = a.next
            b = b.next
        return a
        
    def length(self,head):
        res = 0
        n = head
        while n:
            n = n.next
            res += 1
        return res