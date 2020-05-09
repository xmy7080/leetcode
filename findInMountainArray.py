#lt solution is using 3 binary search, first one is find the peak, next 2 are for find the first index of the target
#https://leetcode.com/problems/find-in-mountain-array/discuss/317607/JavaC%2B%2BPython-Triple-Binary-Search
#pay attention to the different way on binary search, 
#when we need find first occurence that don't hold a func, using the first way of l < r and l = m+1 or r = m -1
#when goal is to exhausted EVERY ele in the sorted array, we need use l <= r and l = m+1 AND r = m -1

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l, r = 0, n-1
        while l < r:
            m = (l + r)//2
            if mountain_arr.get(m) < mountain_arr.get(m+1):
                l = m + 1
                peak = l
            else:
                r = m
        l, r = 0, peak
        while l <= r:
            m = (l + r)//2
            if mountain_arr.get(m) < target:
                l = m + 1
            elif mountain_arr.get(m) > target:
                r = m -1
            else:
                return m
        
        l, r = peak, n-1
        #1,2
        while l <= r:
            m = (l + r)//2
            if mountain_arr.get(m) > target:
                l = m + 1
            elif mountain_arr.get(m) < target:
                r = m -1
            else:
                return m
        return -1
        
