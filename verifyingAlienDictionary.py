class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = {c : i for i, c in enumerate(order)}
        def checkAlphaBe(a, b):
            m, n = len(a), len(b)
            i = 0
            while i <m and i<n:
                if a[i] == b[i]:
                    i += 1
                    continue
                elif idx[a[i]] > idx[b[i]]:
                    return False
                else:
                    return True
            return m < n
        for i in range(len(words)-1):
            if not checkAlphaBe(words[i], words[i+1]):
                return False
        return True
