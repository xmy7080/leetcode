#stack approach, scan from right to left
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        for i in range(len(nums)-1, -1, -1):
            while stk and stk[len(stk)-1] <= nums[i]:
                stk.pop()
            stk.append(nums[i])
        ans = [-1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            while stk and stk[len(stk)-1] <= nums[i]:
                stk.pop()
            ans[i] = stk[len(stk)-1] if stk else -1
            stk.append(nums[i])
        return ans
