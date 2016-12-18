class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        #find the total area
        areaA = (C-A)*(D-B)
        areaB = (G-E)*(H-F)
        #find the overlap area
        xleft = max(A,E)
        xright = min(C,G)
        ybottom = max(B,F)
        ytop = min(D,H)
        overlap = 0
        if xright>xleft and ytop>ybottom:
            overlap = (xright-xleft) *(ytop- ybottom)
        return areaA + areaB - overlap