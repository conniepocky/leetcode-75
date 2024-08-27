class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)

        for r in range(n):
            row = grid[r]
            for c in range(n):
                col = [grid[k][c] for k in range(n)]
                
                if row == col:
                    count += 1

        return count
