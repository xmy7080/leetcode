#===naive way of using stack====
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
        stk1, stk2 = [], []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        
        # head = ListNode(0)
        node = None
        carry = 0
        while stk1 or stk2:
            a = stk1.pop() if stk1 else 0
            b = stk2.pop() if stk2 else 0
            total = a + b + carry
            new = ListNode(total % 10)
            new.next = node
            node = new
            carry = total / 10
        if carry:
            new = ListNode(carry)
            new.next = node
            node = new
        
        return node
            
