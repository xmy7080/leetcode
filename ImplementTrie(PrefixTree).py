class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = collections.defaultdict(TrieNode)
        self.isword = False
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.isword = True
        

    def search(self, word):
        curr = self.root
        for char in word:
            curr = curr.children.get(char)
            if not curr:
                return False
        return curr.isword
        

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            curr = curr.children.get(char)
            if not curr:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")