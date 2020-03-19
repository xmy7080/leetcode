#===keep record of total rotten count from fresh, when two numbers level, exit the loop
#===also when single step didn't convert any orange, stop the loop and return -1
class Solution(object):
    turned = 0
    total = 0
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.turned = 0
        self.total = 0
        for row in grid:
            for o in row:
                if o == 1:
                    self.total += 1
        
        ans = 0
        while self.turned < self.total:
            ans += 1
            if not self.helper(grid):
                break
        return ans if self.turned == self.total else -1
    
    def helper(self, grid):
        roundSet = set()
        def markRot(a, b, roundSet):
            if 0<=a <len(grid) and 0<=b <len(grid[0]) and grid[a][b] == 1:
                roundSet.add((a,b) )
        for i, row in enumerate(grid):
            for j, o in enumerate(row):
                if o == 2:
                    markRot(i+1, j, roundSet)
                    markRot(i-1, j, roundSet)
                    markRot(i, j+1, roundSet)
                    markRot(i, j-1, roundSet)
        self.turned += len(roundSet)
        for p in roundSet:
            grid[p[0]][p[1]] = 2
        return len(roundSet)
        
