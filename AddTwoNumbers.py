# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        head = ListNode(0)
        l3 = head
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0        
            
            sum = num1 + num2 + add
            curval = sum %10
            add = sum/10
            l3.next = ListNode(curval)
            l3 = l3.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if add:
            l3.next = ListNode(add)
            l3 = l3.next
        #l3.val = add
        return head.next