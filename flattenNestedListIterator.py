#Idea is, first flatten the nested list, then iterate like a plain array.
#this is the first solution, there are also solution using stack and others
#https://leetcode.com/articles/flatten-nested-iterator/
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flatten(nested):
            for ele in nested:
                if ele.isInteger():
                    self.numbers.append(ele.getInteger())
                else:
                    flatten(ele.getList())
        self.numbers = []
        self.idx = 0
        flatten(nestedList)
        self.lth = len(self.numbers)
    
    def next(self) -> int:
        output = self.numbers[self.idx]
        self.idx += 1
        return output
        
    def hasNext(self) -> bool:
        return self.idx < self.lth

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
