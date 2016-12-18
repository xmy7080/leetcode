# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return None
        slow = head
        fast = head
        hascycle = False
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None
            if fast is slow:
                hascycle = True
                break
        if not hascycle: return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow