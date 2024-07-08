from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: 
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        result = 0

        while rotten and fresh:
            for _ in range(len(rotten)):
                x,y = rotten.popleft()
                for coord in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)): #find adjacent oranges/cells
                    if coord in fresh:
                        fresh.remove(coord)
                        rotten.append(coord)
            
            result += 1

        return -1 if fresh else result
