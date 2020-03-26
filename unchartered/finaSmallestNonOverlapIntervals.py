byte dance

3/26 phone interview
 

Given a collection of intervals
One interval may include another interval, but there is no overlapping
For example,
    [1, 10] includes [2, 3], [4, 5]
    [2, 5]  overlaps [4, 6]

1. Design the structure to store intervals, and do best(smallest) match for given numbers.
    For example,
    Input:
        Intervals: [[2, 3], [1, 20], [15, 16], [2, 5], [1, 8], [9, 12], [6, 8]]         Numbers: [3, 5, 7, 9, 15, 17, 40]
    Output:
        [[2, 3], [2, 5], [6, 8], [9, 12], [15, 16], [1, 20], []]
    Explanation:
        3 is in [2, 3], [1, 20], [2, 5], [1, 8]     best match -> [2, 3]
        5 is in [2, 5], [1, 20],                    best match -> [2, 5]
        7 is in [1, 8], [6, 8], [1, 20]             best match -> [6, 8]
        ...

2. For M intervals and N numbers, what's time complexity of your code?
3. How can you improve the algorithm in your code?
#=========================
[1, 10]: [2, 3], [4, 5]

class interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.children = []

def findNext(self, m, n, span):
    ans = []
    i = m
    while i < n:
        newItv = interval(span[i][0], span[i][1])
        j = i+1
        while j<n and intervals[j][1] <= span[1]:
            j += 1
        newItv.children = findNest(i+1, j, span)
        ans.append(newItv)
        i = j+1
    return ans

def contains():

def dfs(self, span, n):
    l = 0, r = len(span)
    while l < r:
        mid = (l+r)/2
        s = span[mid]
        if contains(s, n):
            if not s.children:
                return [s.a, s.b]
            return dfs(s, n)
        if n < s.a:
            r = mid
        if n > s.b:
            l = mid
    return []
    
    
def bestSmallest(self, intervals, numbers):
    lth = len(intervals)
    #bigger interval go ahead when left bound is same
    intervals.sort(key = lambda x: (x[0], -x[1]))
    itvs = findNest(0, lth, intervals)
    ans = []
    for n in numbers:
        ans.append(dfs(itvs, n))
    return ans
