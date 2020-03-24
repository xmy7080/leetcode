#solution https://leetcode.com/articles/swap-adjacent-in-lr-string/
#add extra check on number of X
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.count('X') != end.count('X'):
            return False
        if start.replace('X', '') != end.replace('X', ''):
            return False
        t = 0
        for i, n in enumerate(start):
            if n == 'L':
                while end[t] != 'L': t += 1
                if i < t: #nth L in "end" has move to the right of correspond L in "start", which is impossible
                    return False
                t += 1
        t = 0
        for i, n in enumerate(start):
            if n == 'R':
                while end[t] != 'R': t += 1
                if i > t: #nth R in "end" has move to the left of correspond R in "start", which is impossible
                    return False
                t += 1
        
        return True
