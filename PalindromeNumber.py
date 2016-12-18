class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0: return False
        tens = 1
        modten = x/tens
        while modten >= 10:
            tens *= 10
            modten = x/tens
        ones = 1
        
        while tens> ones:
            i = x/tens % 10
            j = x/ones % 10
            if i != j: return False
            tens = tens/10
            ones = ones *10
        return True