import collections
class Movie(object):
    def __init__(self, id, rating):
        self.id = id
        self.rating = rating
        self.similarMovies = []
mulhollandDR = Movie("mulhollandDR", 8.9)
triagle = Movie("triagle", 8.7)
sixSense = Movie("sixSense", 8.8)
sevenSins = Movie("sevenSins", 9.0)

mulhollandDR.similarMovies = [triagle, sixSense]
triagle.similarMovies = [mulhollandDR, sevenSins]
sixSense.similarMovies = [mulhollandDR, sevenSins]
sevenSins.similarMovies = [sixSense, triagle]

import heapq
def kHighestRatingMovies(m, K):
    kHigh = []
    round = set([m])
    visited = set([m])
    while round:
    	newR = set()
        print ("loop")
        print (round)
        print (visited)
    	for start in round:
            for mov in start.similarMovies:
                if mov not in visited:
                    newR.add(mov)
    		if start not in visited:
    			if len(kHigh) < K:
    				heapq.heappush(kHigh, (start.rating, start.id))
    			else:
    				heapq.heappushpop(kHigh, (start.rating, start.id))
    		visited.add(start)
    	round = newR
    return kHigh
    
print (kHighestRatingMovies(mulhollandDR, 5))
