class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        #input check
        #wordList is empty
        #begin == end
        if beginWord == endWord: return 1
        
        #bfs, maintain 2 queues
        from collections import deque
        qcurr = deque()
        qtmp = deque()
        qcurr.append(beginWord)
        steps = 2
        #loop
        while qcurr or qtmp:
            if not qcurr:#put tmp queue to current queue
                qcurr = qtmp
                qtmp = deque()
            while qcurr:
                #alternating
                word = qcurr.popleft()
                for i in xrange(len(word)):#for "hit", i will be inside [0,1,2]
                    for j in [chr(c+ord('a')) for c in xrange(26) ]:
                        if j == word[i]: continue
                        altered = word[:i]+ j + word[i+1:]
                        #check the altered is end word
                        if altered == endWord: return steps
                        #check the altered is in word list
                        if altered in wordList:
                            qtmp.append(altered)
                            wordList.remove(altered)
            steps += 1
        return 0