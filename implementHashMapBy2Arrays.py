#It has been pointed out the average search, insert and delete functions shall be O(1) for Hashtable. 
#So the below implementation is not strictly hashtable by definition. 
#Though the question itself does not explicitly state the time complexity requirement and it gets passed for all test cases
class MyHashMap(object):

    def __init__(self):
        self.keys = []
        self.values = []
        
    def put(self, key, value):
        if key in self.keys:
            self.values[self.keys.index(key)] = value
        else:
            self.keys.append(key)
            self.values.append(value)
        
    def get(self, key):
        if key in self.keys:
            return self.values[self.keys.index(key)]
        else:
            return -1
        
    def remove(self, key):
        if key in self.keys:
            del self.values[self.keys.index(key)]
            del self.keys[self.keys.index(key)] 
