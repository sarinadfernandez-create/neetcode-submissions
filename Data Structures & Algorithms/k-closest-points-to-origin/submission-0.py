import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distFromOrigin(coords):
            x,y = tuple(coords)
            return (x**2 + y**2)
        
        h = []
        heapq.heapify(h)

        for p in points:
            heapq.heappush(h, (-distFromOrigin(p),p))
            while len(h)>k:
                heapq.heappop(h)

#key takeaway, heaps always sort tuples by first value.
        return [point for dist, point in h]