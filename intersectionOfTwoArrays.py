class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1, dic2 = collections.defaultdict(int), collections.defaultdict(int)
        for n in nums1:
            dic1[n] += 1
        for n in nums2:
            dic2[n] += 1
        ans = []
        if len(dic1) < len(dic2):
            for key in dic1:
                ans += [key] * min(dic1[key], dic2.get(key,0) )
        else:
            for key in dic2:
                ans += [key] * min(dic2[key], dic1.get(key,0) )
        return ans
        
