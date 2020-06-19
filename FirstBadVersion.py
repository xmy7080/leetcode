# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while l <= r:
            mid = (l+r)//2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                r = mid-1
            else:
                l = mid + 1
        
#==========
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, last = 1, n
        while first<last:
            mid = first + (last-first)/2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1
        return first
