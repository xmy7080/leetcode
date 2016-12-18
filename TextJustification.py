class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        #if not maxWidth: return [""]
        rest = maxWidth
        lines, line = [], []
        for w in words:
            if rest == maxWidth:
                #first word in first line
                rest = maxWidth - len(w)
                line.append(w)
            elif rest > len(w):
                #packing words
                rest -= len(w) + 1
                line.append(' '+w)
            elif rest <= len(w):
                #apply the extra spaces
                nOfWordNeedPacking = len(line)-1
                if not nOfWordNeedPacking:
                    lines.append(''.join(line) + ' '*rest)
                    rest, line = maxWidth - len(w), [w]
                    continue
                evenPacking = rest/ nOfWordNeedPacking
                oneMorePackings = rest % nOfWordNeedPacking
                for i in range(1,len(line)):
                    if i <= oneMorePackings:
                        line[i] = ' '*(evenPacking + 1) +line[i]
                    else:
                        line[i] = ' '*evenPacking +line[i]
                #close this line and start the next line
                lines.append(''.join(line))
                rest, line = maxWidth - len(w), [w]
        lines.append(''.join(line)+' '*rest)
        return lines