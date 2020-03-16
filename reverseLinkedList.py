# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# think each link as a layer of recursive call, so on the last return call on node 1, we got have the newHead, all the way from the tail node
# hence we pass along the newHead all the way up
# then between each two nodes, say 4 and 5, after we got the newHead, now it's safe to modify next node status. 
# we can set 4.next.next to 4 itself it gonna created a loop like
#   <-
#  /  \
# 4 --> 5
# lastly, since we don't know if 4 is the original head, we should assume 4 don't have next, i.e. 4.next = None,
# hence the loop above will eventually be
#            <-
#           /  \
# None <-- 4     5
# which is exactly what we looking for. right now we can safely say, when this recursive ends, we will reverse all nodes.
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
