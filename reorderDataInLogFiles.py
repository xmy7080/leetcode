#amazon oa
#https://leetcode.com/articles/reorder-log-files/
#pay attention on the usage of log.split(' ', 1), it actually only cut first piece out and rest will remains
#also .isalpha() and .isdigit()
#if comparable func is all (1,) the order will remains, in this case the digits logs does.
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            iden, rest = log.split(' ', 1)
            return (0, rest, iden) if rest[0].isalpha() else (1, )
        return sorted(logs, key = f)
        # alpha, digit = [], []
        # for log in logs:
        #     identifier, words = log.split(" ", 1)
        #     if words[0].isdigit():
        #         digit.append(log)
        #     else:
        #         alpha.append((words, identifier, log) )
        # ans = []
        # for tpl in sorted(alpha):
        #     ans.append(tpl[2])
        # return ans + digit
