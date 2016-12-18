class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        i,j = 0,l-1
        while i <j:
            while not s[i].isalnum() and i<j: 
                i += 1
            while not s[j].isalnum() and j>i:
                j -= 1
            if i>=j: break
            else:
                if s[i].lower() != s[j].lower():
                    return False
            i += 1
            j -= 1
        return True