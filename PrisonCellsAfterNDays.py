#mine solution, faster
# bear in mind that loop probably won't start from the first num, so a dictionary of what has appear is necessary
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        num = reduce((lambda x,y: x*2 + y), cells)
        seen = {}
        while N:
            seen[num] = N
            shiftL, shiftR = num << 1, num >> 1
            num = ~ (shiftL ^ shiftR) & int('01111110',2)
            N -= 1
            if num in seen:
                N = N % (seen[num] - N)
        
        mask = int('10000000', 2)
        res = []
        while mask:
            res.append(num & mask and 1)
            mask >>= 1
        return res
    
    # leetcode solution, slower
# class Solution(object):
#     def prisonAfterNDays(self, cells, N):
#         def nextday(cells):
#             return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1])
#                     for i in xrange(8)]

#         seen = {}
#         while N > 0:
#             c = tuple(cells)
#             if c in seen:
#                 N %= seen[c] - N
#             seen[c] = N

#             if N >= 1:
#                 N -= 1
#                 cells = nextday(cells)

#         return cells
    
