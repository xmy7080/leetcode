#======O(n logn) solution, jiuzhang dp lesson 7
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, A):
        # write your code here
        if not A: return 0
        #f: 0 1 2 3 4
        #a: -inf 10 20 30 ...
        B = [0] * (len(A)+1)
        Btop = 0
        B[0] = -sys.maxint-1
        start, stop, mid, last = 0,0,0,0
        for i in xrange(len(A)):
            #find in B the biggest number that is smaller than A[i]
            start, stop = 0, Btop
            while(start <= stop):
                mid = (start + stop)/2
                if B[mid] < A[i]:
                    last = mid #save mid as one candidate
                    start = mid + 1
                else:
                    stop = mid -1
            
            B[last + 1] = A[i]
            #when B[] are growing, Btop += 1
            if last + 1 > Btop:
                Btop += 1
        return Btop
#======new O(n^2) solution, from jiuzhang dp 坐标型=====
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums): return 0
        dp = [0] * len(nums)
        for i in xrange(len(nums)):
            dp[i] = 1
            for j in xrange(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
#======old O(n^2) solution===
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #check input
        l = len(nums)
        if l <=1: return l
        #fill each lenth of increase as base "1"
        li = [1] * l
        for i in xrange(l):
            for j in xrange(0,i):
                if nums[j] < nums[i]:# if curr num add one more increse length, try update li[i]
                    if li[j] + 1 > li[i]:
                        li[i] = li[j]+1
        return max(li)
