class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.sub(r'[^\w\s]+',' ',paragraph)
        words = re.compile("[\s]+").split(paragraph)
        if words[-1] == "":
            words = words[:-1]
        dic = collections.defaultdict(int)
        mostFreqW = ("",0)
        for w in words:
            w = w.lower()
            if w not in banned:
                dic[w] += 1
                if mostFreqW[1] < dic[w]:
                    mostFreqW = (w, dic[w])
        return mostFreqW[0]
