class Vector2D(object):

    
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.v2d = vec2d
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        num = self.v2d[self.i][self.j]
        self.j += 1
        return num
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < len(self.v2d):
            if self.j < len(self.v2d[self.i]):
                return True
            else:
                self.j = 0
                self.i += 1
        return False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
