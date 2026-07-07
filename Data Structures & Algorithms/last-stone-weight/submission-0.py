import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = [-s for s in stones]
        heapq.heapify(self.heap)
        
        while len(self.heap) > 1:
            stone1 = heapq.heappop(self.heap)
            stone2 = heapq.heappop(self.heap)
            diffstone = stone1 - stone2
            
            if diffstone != 0:
                heapq.heappush(self.heap, diffstone)
        
        return abs(self.heap[0]) if self.heap else 0