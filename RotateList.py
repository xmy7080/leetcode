# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        tmp = head
        length = 1
        while tmp.next:
            tmp = tmp.next
            length +=1
        k = k%length
        l1 = head
        l2 = head
        for i in range(k):
            if l2.next:
                l2 = l2.next
            else:
                break
        while l2.next:
            l1 = l1.next
            l2 = l2.next
        l2.next = head
        head = l1.next
        l1.next = None
        return head