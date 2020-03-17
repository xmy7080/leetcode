#=======above is the version don't only make shallow copy=======
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        while l1 and l2:
            if l1.val < l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else :
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next
        while l1:
            node.next = ListNode(l1.val)
            node = node.next
            l1 = l1.next
        while l2:
            node.next = ListNode(l2.val)
            node = node.next
            l2 = l2.next
        return head.next
            
#============version of shallow copy=====
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = ListNode(0)
        res = h
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        if l1:
            res.next = l1
        elif l2:
            res.next = l2
        return h.next
