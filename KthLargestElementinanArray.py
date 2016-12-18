class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []#maintain a k size max heap
        for n in nums:
            if len(heap) == k and n>heap[0]: 
                #when heap is full to k, and n bigger than the smallest in heap, replace n with it
                heapq.heapreplace(heap,n)
            elif len(heap) < k:
                #when heap is not fill to k size
                heapq.heappush(heap,n)
        return heap[0]
        