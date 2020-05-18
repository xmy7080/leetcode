#a very neat trie solution https://leetcode.com/problems/search-suggestions-system/discuss/436151/JavaPython-3-Simple-Trie-and-Binary-Search-codes-w-comment-and-brief-analysis.
class Trie:
    def __init__(self):
        self.sub = {} #save next level subtrees
        self.suggestion = [] #save the first 3 suggestion words
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = Trie()
        for product in sorted(products):
            trie = root
            for char in product:
                if char not in trie.sub:
                    trie.sub[char] = Trie()
                trie = trie.sub[char]
                if len(trie.suggestion) < 3:
                    trie.suggestion.append(product)
        ans = []
        for char in searchWord:
            if root:
                root = root.sub.get(char, None)
            ans.append(root.suggestion if root else [] )
        return ans
