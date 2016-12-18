class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        num = [str(n) for n in nums]
        num.sort(cmp = lambda x,y:cmp(y+x,x+y))
        return ''.join(num).lstrip('0') or '0'
        