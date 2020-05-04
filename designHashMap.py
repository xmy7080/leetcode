#this is a real hashmap implementation, with O(1) manipulation time
#leetcode solution https://leetcode.com/articles/design-hashmap/
class Bucket:
    def __init__(self):
        self.bucket = []
        
    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                found = True
                self.bucket[i] = (key, value)
                return
        if not found:
            self.bucket.append((key, value) )
    
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if kv[0] == key:
                del self.bucket[i]
                return
        
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 2069
        self.hashTable = [Bucket() for _ in xrange(self.capacity) ]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hashCode = key % self.capacity
        self.hashTable[hashCode].update(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashCode = key % self.capacity
        return self.hashTable[hashCode].get(key)
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hashCode = key % self.capacity
        self.hashTable[hashCode].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
