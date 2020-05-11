#lt solution
#https://leetcode.com/articles/time-based-key-value-store/
#be aware that for bisect binary search to work correctly, we need chr(127) or chr(126)'~'(may not work) as the biggest char that can rank after any string
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value) )
        

    def get(self, key: str, timestamp: int) -> str:
        val = self.M.get(key, None)
        if not val: return ""
        i = bisect.bisect(val, (timestamp, '~'))
        return val[i-1][1] if i else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
