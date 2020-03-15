# collection.deque are a doule-linked list based queue, which have O(1) of append, prepend, pop and popleft
# so in this case, we combine it with a dictionary, which saved the mapping information between key and value.
# and deque serves as a record of which been access most recent (last one in the queue) vs least recent (first one in the queue)
class LRUCache(object):
    def __init__(self, capacity):
        self.q = collections.deque()
        self.d = {}
        self.capacity = capacity

    def get(self, key):
        if key in self.d:
            self.q.remove(key)
            self.q.append(key)
            return self.d[key]
        return -1

    def set(self, key, val):
        if key in self.d:
            self.q.remove(key)
        elif len(self.d) == self.capacity:
            rmv = self.q.popleft()
            del self.d[rmv]
        self.q.append(key)
        self.d[key] = val
        return























    # def __init__(self, capacity):
    #     self.q = collections.deque()
    #     self.dic = {}
    #     self.capacity = capacity
        

    # def get(self, key):
    #     if key not in self.q:
    #         return -1
    #     self.q.remove(key)
    #     self.q.append(key)
    #     return self.dic[key]
        

    # def set(self, key, value):
    #     if key in self.q:
    #         self.q.remove(key)
    #     elif len(self.q) == self.capacity:
    #         dump = self.q.popleft()
    #         self.dic.pop(dump)
    #     self.q.append(key)
    #     self.dic[key] = value
        
        
        
        # class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.dic = {}
#         self.q = collections.deque([])
#         self.capa = capacity
        

#     def get(self, key):
#         """
#         :rtype: int
#         """
#         if key not in self.dic:
#             return -1
#         self.q.remove(key)
#         self.q.append(key)
#         return self.dic[key]
        

#     def set(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: nothing
#         """
#         if key in self.dic:
#             self.q.remove(key)
#         elif len(self.dic) == self.capa:
#             v = self.q.popleft()
#             self.dic.pop(v)
#         self.q.append(key)
#         self.dic[key] = value
