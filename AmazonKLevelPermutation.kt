Find K-Level Permutation
You have an array from 1 to N now you have to find a K-level permutation such that for N-K+1 segments or windows you get the difference between sum of maximum segment sum and minimum segment must be at most 1.

Example 1:

Input:  N = 7, K = 4
Output: [1, 7, 3, 5, 2, 6, 4] 
Explanation:
[1,7,3,5] + 1 = [7,3,5,2] = [3,5,2,6] + 1 = [5,2,6,4]
      
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
res = []

class Solution:
    
    def findKLevelPermutation(self, N: int, K: int):
        global res
        res = []
        tmp = []
        not_picked = set(range(1, N + 1))
        self.dfs(not_picked, tmp, N, K, 0)
        return res
        
    def dfs(self, not_picked, tmp, N, K, lastMove):
        global res
        if len(tmp) == N:
            if abs(tmp[-1] - tmp[(- K - 1)]) <= 1:
                res += [tmp[:]]
                print(tmp)
                # print('\n')
                return
            else: 
                return
        if len(tmp) < K : # when search not over 1 segment
            for value in range(1, N+1):
                if value in not_picked: 
                    tmp.append(value)
                    not_picked.remove(value)
                    self.dfs(not_picked, tmp, N, K, 0)
                    not_picked.add(value)
                    tmp.pop()
        
        if len(tmp) >= K and len(tmp) < N: # when search is over 1 segment, less possible selection ( +- 1 of tmp[- K])
            retroVal = tmp[-1 * K]
            # print(tmp[-1])
            if lastMove <= 0 and retroVal + 1 <= N and retroVal + 1 in not_picked:
                tmp.append(retroVal + 1)
                not_picked.remove(retroVal + 1)
                self.dfs(not_picked, tmp, N, K, 1)
                not_picked.add(retroVal + 1)
                tmp.pop()
            if lastMove >= 0 and retroVal - 1 > 0 and retroVal - 1 in not_picked:
                tmp.append(retroVal - 1)
                not_picked.remove(retroVal - 1)
                self.dfs(not_picked, tmp, N, K, -1)
                not_picked.add(retroVal - 1)
                tmp.pop()

solu = Solution()
solu.findKLevelPermutation(7, 3)
