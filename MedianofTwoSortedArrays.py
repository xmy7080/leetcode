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
        
        
        
        
        
        