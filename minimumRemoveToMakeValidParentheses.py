#lt solution, record all the index of invalid ')', and rest in the stk is the '(' need to be removed
#https://leetcode.com/articles/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removeSet = set()
        stk = []
        for i, c in enumerate(s):
            if c not in (')','('):
                continue
            elif c == '(':
                stk.append(i)
            elif not stk:
                removeSet.add(i)
            else:
                stk.pop()
        removeSet = removeSet.union(set(stk))
        ans = []
        for i, c in enumerate(s):
            if i not in removeSet:
                ans.append(c)
        return ''.join(ans)
