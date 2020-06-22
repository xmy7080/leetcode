#https://leetcode.com/articles/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = collections.defaultdict(int)
        ans, tot = 0, 0
        dic[0] = 1
        for n in nums:
            tot += n
            if tot-k in dic:
                ans += dic[tot-k]
            dic[tot] += 1
        return ans
