# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return -1
        if n == 1: return 1
        possible = 0
        for i in xrange(1, n):
            if knows(possible, i):
                possible = i
        for i in xrange(n):
            if i == possible: continue
            if knows(possible, i):
                return -1
            if not knows(i, possible):
                return -1
        return possible
                
