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
    
    #==========recursive way, not very easy to implement, before look this, take a look at recursive way in reverse linked list I ====
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
        if not head or not head.next or m == n:
            return head
        return self.helper(head, None, m, n)
        
    def helper(self, node, mTail, m, n):
        if m > 2: #not started tackle the problem
            self.helper(node.next, None, m-1, n-1)
            return node
        elif m == 2: #set front node next to nHead
            nHead = self.helper(node.next, None, m-1, n-1)
            node.next = nHead
            return node
        elif m == 1: #pass mTail in the recursive func, do not set mTail.next to None, cause it  already set to next node after mTail within the recursive
            nHead = self.helper(node.next, node, m-1, n-1)
            # node.next.next = node
            # node.next = None
            return nHead
        elif m == 0 and n > 1: #node next to mTail, need set node.next = mTail
            nHead = self.helper(node.next, mTail, m-1, n-1)
            node.next.next = node
            node.next = mTail
            return nHead
        elif m == 0 and n == 1: #tackle [3,5] 1,2 case, on the both cases of "node next to mTail" and "return curr as nHead"
            self.helper(node.next, mTail, m-1, n-1)
            node.next = mTail
            return node
        elif m < 0 and n > 1: #normal stuff 
            nHead = self.helper(node.next, mTail, m-1, n-1)
            node.next.next = node
            node.next = None
            return nHead
        elif n == 1: #return curr as nHead, keep passing mtail to next
            self.helper(node.next, mTail, m-1, n-1)
            return node
        elif n == 0: # put curr as mTail next, stop call helper function, reverse work done
            mTail.next = node
