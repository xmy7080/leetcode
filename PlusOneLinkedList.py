# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = ListNode(0)
        i = j = newhead
        newhead.next = head
        
        while j.next:#find first non 9 digit start from tail, name it i
            j = j.next
            if j.val != 9:
                i = j
        
        if j.val != 9:#if last digit has margin, != 9, just add one on it
            j.val += 1
        else:#if there are ...999 at end, name it ends at ..1000
            i.val += 1
            i = i.next
            while i:
                i.val = 0
                i = i.next
        
        if newhead.val == 0:#if not the case like 9999
            return newhead.next
        return newhead#if case 9999