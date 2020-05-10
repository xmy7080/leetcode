#easy to digest solution, basically binary find how many a from A (longer arr) will contribute to final first half of array
#code derived from this solution https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            tmp = nums2
            nums2 = nums1
            nums1 = tmp
        #nums1 is now the longer one, l1 > l2
        l1, l2 = len(nums1), len(nums2)
        
        isOdd = (l1 + l2) % 2
        medianCount = (l1 + l2)//2 + 1
        
        #nums1's min contribution and max contribution
        l, r = medianCount-l2, medianCount
        while l <= r:
            aCount = l + (r-l)//2
            bCount = medianCount - aCount
            
            alast = nums1[aCount-1]
            blast = nums2[bCount-1] if bCount > 0 else None
            anext = nums1[aCount] if aCount < l1 else None
            bnext = nums2[bCount] if bCount < l2 else None
            #nums1 last is bigger than nums2's next ele not in selection, shink nums1
            if bnext and alast > bnext:
                r = aCount - 1
                continue
            #nums2 last is bigger than nums1's next ele not in selection, shink nums2
            if anext and blast and blast > anext:
                l = aCount + 1
                continue
            if isOdd:
                return max(alast, blast) if blast else alast
            else:
                #this is just find the last2 from each contributing arr, sort them and find out 2 biggest out of 4, then calculate is average
                alast2 = nums1[aCount-2 if aCount >1 else 0: aCount]
                blast2 = nums2[bCount-2 if bCount >1 else 0: bCount]
                # print(str(alast2) + ' ' + str(blast2))
                return sum( sorted(alast2 + blast2)[-2:] )/2
                # #when total is even, we need discuss [1,2] and [-1]case and [1,5] [3] case
                # if blast:
                #     if aCount > 1:
                #         return (alast + blast)/2 if nums1[aCount-2] < blast else (alast + nums1[aCount-2])/2
                #     else:
                #         return (alast + blast)/2
                # else:
                #     return (alast + nums1[aCount-2])/2
                    
                # return (alast + blast)/2 if blast and nums1[aCount-2] < blast else (alast + nums1[aCount-2])/2
        return -1
        
#older solution, forget where it come from
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        k = (m+n+1)/2
        median = self.getkth(nums1,0,m-1, nums2,0,n-1, k)
        
        if (m+n)%2 == 0:
            k2 = k+1
            median2 = self.getkth(nums1,0,m-1, nums2,0,n-1, k2)
            median = (median + median2)/2.0
        return median
        
    #     // find the kth element int the two sorted arrays
    # // let us say: A[aMid] <= B[bMid], x: mid len of a, y: mid len of b, then wen can know
    # // 
    # // (1) there will be at least (x + 1 + y) elements before bMid
    # // (2) there will be at least (m - x - 1 + n - y) = m + n - (x + y +1) elements after aMid
    # // therefore
    # // if k <= x + y + 1, find the kth element in a and b, but unconsidering bMid and its suffix
    # // if k > x + y + 1, find the k - (x + 1) th element in a and b, but unconsidering aMid and its prefix
    def getkth(self, a, al, ar, b, bl, br, k):
        if al > ar: return b[bl+k-1]
        if bl > br: return a[al+k-1]
        
        amid = (al + ar)/2
        bmid = (bl + br)/2
        
        if a[amid] <= b[bmid]:
            if k > (amid-al) + (bmid-bl) + 1:
                return self.getkth(a, amid+1, ar, b, bl,br, k-(amid-al)-1)
            else:
                return self.getkth(a, al, ar, b, bl, bmid-1, k)
        else:
            if k > (amid-al) + (bmid-bl) + 1:
                return self.getkth(a, al, ar, b, bmid+1,br, k-(bmid-bl)-1)
            else:
                return self.getkth(a, al, amid-1, b, bl, br, k)
        
        
        
        
        
        
