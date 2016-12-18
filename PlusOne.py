class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)-1
        carry = 0
        sum = 1
        while l >= 0:
            sum += digits[l] + carry
            digits[l] = sum % 10
            carry = sum/10
            sum = 0
            l -= 1
        if carry == 1:
            digits[0:0] = [1]
        return digits