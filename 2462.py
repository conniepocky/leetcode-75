class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        left = 0
        right = len(costs)-1
        heap1 = []
        heap2 = []

        ans = 0

        for _ in range(k):
            while left <= right and len(heap1) < candidates:
                heapq.heappush(heap1, costs[left])
                left += 1

            while left <= right and len(heap2) < candidates:
                heapq.heappush(heap2, costs[right])
                right -= 1 

            if not heap1:
                x = maxsize
            else:
                x = heap1[0]

            if not heap2:
                y = maxsize
            else:
                y = heap2[0]

            if x <= y:
                ans += heapq.heappop(heap1)
            else:
                ans += heapq.heappop(heap2)

        return ans
        
