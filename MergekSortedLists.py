# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heapify,heapreplace,heappop,heappush
        dummy = ListNode(0)
        node = dummy
        h = [(n.val,n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if not n.next:
                heappop(h)
            else:
                heapreplace(h,(n.next.val,n.next))
            node.next = n
            node = node.next
        return dummy.next
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # from heapq import heapify, heappop, heapreplace, heappush
        # node = dummy = ListNode(0)
        # h = [(n.val,n) for n in lists if n]
        # heapify(h)
        # while h:
        #     v,n = h[0]
        #     if not n.next:
        #         heappop(h)
        #     else:
        #         heapreplace(h,(n.next.val,n.next))
        #     node.next = n
        #     node = node.next
        # return dummy.next