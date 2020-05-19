#easy to understand lt solution
#https://leetcode.com/articles/partition-labels/

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        anchor = j = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(j - anchor + 1)
                anchor = i + 1
        return ans
