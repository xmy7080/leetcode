class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = []
        for n in nums:
            if n in heap:
                continue
            if len(heap) == 3  and n > heap[0]:
                heapq.heapreplace(heap,n)
            elif len(heap) < 3:
                heapq.heappush(heap,n)
        return heap[0] if len(heap) == 3 else heap[len(heap)-1]