import collections
# tag_list = ["made","in","china"]
tag_list = ["made"]
all_tags = ["made", "a","b","c","in", "china","made","b","c","d"]
import heapq
def shortestSubsequenceTags(target, al):
    need, missing = collections.defaultdict(int), len(target)
    for c in target:
        need[c] += 1
    i = I = J = 0
    for j, c in enumerate(al, 1):
        if c in need:
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
        while not missing:
            if al[i] in need:
                need[al[i]] += 1
                if need[al[i]] > 0:
                    missing += 1
            if not J or j -i < J - I:
                I, J = i, j
            i += 1
            
    return [I, J-1]
    
print (shortestSubsequenceTags(tag_list, all_tags))
