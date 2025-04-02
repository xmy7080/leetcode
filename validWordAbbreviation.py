class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        w, a = 0, 0
        whichNumberic = 0
        while a < len(abbr) and w < len(word):
            if (whichNumberic == 0 and abbr[a] == '0'): return False 
            if abbr[a].isdigit():
                whichNumberic = whichNumberic * 10 + ord(abbr[a]) - ord('0')
                a += 1
            else: # curr char is non-numeric
                if whichNumberic: # if we have cached numeric value
                    w += whichNumberic
                    whichNumberic = 0
                else: # no chached numeric value
                    if word[w] != abbr[a]: return False
                    w += 1
                    a += 1
        if whichNumberic:
            w += whichNumberic
        return True if a == len(abbr) and w == len(word) else False
