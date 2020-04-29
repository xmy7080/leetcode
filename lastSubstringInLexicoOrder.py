#easiest solution from this link
#https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/363662/Short-python-code-O(n)-time-and-O(1)-space-with-proof-and-visualization/408434
class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        i, j, k = 0, 1, 0
        while j + k < n:
            if s[i+k] == s[j+k]:
                k += 1
            elif s[i+k] < s[j+k]:
                i = j
                j += 1
                k = 0
            else:
                j += k+1
                k = 0
        return s[i:]
        
        #O(n^2) solution, will timeout
#         def lessThan(s, t):
#             ls, lt  = len(s), len(t)
#             a, b = 0, 0
#             while a < ls and b < lt:
#                 if s[a] < t[b]:
#                     return True
#                 elif s[a] > t[b]:
#                     return False
#                 a += 1
#                 b += 1
#             # print(ls)
#             # print(lt)
#             return ls < lt
#         l = len(s) -1
#         ans = s[l:]
#         while l >= 0:
#             if ans[0] <= s[l]:
#                 # print(s[l])
#                 if lessThan(ans, s[l:]):
#                     ans = s[l:]
#             l -= 1
#         return ans
            
