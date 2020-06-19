#easy solution
#https://leetcode.com/problems/valid-palindrome-ii/discuss/107718/Easy-to-Understand-Python-Solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        def isPalin(a: str) -> bool:
            return a[:] == a[::-1]
        while l < r:
            if s[l] != s[r]:
                #discuss [l:r-1] case and [l+1, r] case
                return isPalin(s[l:r]) or isPalin(s[l+1: r+1])
            l += 1
            r -= 1
        return True
