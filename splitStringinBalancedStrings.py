class Solution:
    def balancedStringSplit(self, st: str) -> int:
        s, ans = 0, 0
        for c in st:
            if c == 'R':
                s += 1
            else:
                s -= 1
            if not s:
                ans += 1
        return ans
        
