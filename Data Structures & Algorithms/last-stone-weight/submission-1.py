import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #think we can just treat the list of stones as a heap
        #we have to pop the heaviest stones though so
        reversedStones = [0]*len(stones)
        for i in range(len(stones)):
            reversedStones[i] = -1 * stones[i]
        heapq.heapify(reversedStones)
        while len(reversedStones)>1:
            stone1=heapq.heappop(reversedStones)
            stone2=heapq.heappop(reversedStones)
            if stone1==stone2:
                pass
            else:
                heapq.heappush(reversedStones, -1 * abs(stone1-stone2))
        if reversedStones:
            return -1 * heapq.heappop(reversedStones)
        return 0